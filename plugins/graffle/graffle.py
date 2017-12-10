import os
import re
import warnings
import omnigraffle_export
import subprocess

class Job(object):
    def __init__(self, dst_img, canvasname):
        self.dst_img = dst_img
        self.canvasname = canvasname

class GrafflePlugin(object):

    def __init__(self, preprocessor):
        self.pp = preprocessor
        self.token = "graffle"
        self.pp.register_plugin(self)
        self.graffle = {}
        self.comment_gid = 0 # global comment ID for relative refs in this file.
        self.jobs = {}

    def process(self, code, fname, canvasname, title=None, format='svg', div_style=None):
        """
        Open up a specific tab of an visio file and dump it to png

        ```graffle("fname", "canvasname", "Optional Title")
        """

        if title is None: title = canvasname

        dstfile = fname

        # Pull from the web if the user wants it
        if (fname.startswith("http")):
            try:
                dstfile = save_url(fname, os.path.join(self.dirs[-1], self.auto))
            except Exception as e:
                traceback.print_exc()
                # deal with a bad URL
                return "[%s <mark>_file not found_</mark>](%s)" % (title, fname)

        grafflefile, graffle_relative = self.pp.get_asset(dstfile, True)

        # Export to the output file
        fname = os.path.split(grafflefile)[1]
        imgname = os.path.join(self.pp.auto_dir(), self.pp.tofname("%s_%s" % (fname, canvasname), graffle_relative) + '.' + format)

        # TODO: implement doc server locally here and have the main engine stall on completion.
        # For now, just convert the entire graffle speculatively
        """
        # Add the file/page to the convert "queue"
        if grafflefile not in g.graffle2convert:
            g.graffle2convert[grafflefile] = []

        job = {"page": canvasname, "fnout": imgname, "title": title}
        g.graffle2convert[visiofile].append(job)
        """

        # Remember this job
        if (not self.jobs.has_key(grafflefile)):
            self.jobs[grafflefile] = []

        # queue this job
        self.jobs[grafflefile].append(Job(imgname, canvasname))

        return self.pp.img2md(imgname, title, div_style)

    def export_graffle(self, graffle_file, jobs):
        """
        Construct the applescript commands and execute
        """
        # First, build the core commands per canvas.
        canvas_save = ""
        for j in jobs:
            # Only run this if the source file is newer than the dst.
            if self.pp.exists_and_newer(j.dst_img, graffle_file):
                continue
            canvas_save += graffle_export_canvas % (j.canvasname, macpath(j.dst_img))
            
        if canvas_save == "":
            # nothing to do
            return

        ascript = graffle_export_script % (macpath(graffle_file), canvas_save)
        lines = ascript.strip().split("\n")
        cmd = ""
        for line in lines:
            # skip empty lines
            if line.strip() == "": continue
            cmd += "-e \"%s\" " % line.strip().replace('"', r'\"')
        self.pp._call("osascript %s" % cmd)

        # Timestamp the outputs
        for j in jobs:
            self.pp.timestamp(j.dst_img)

    def preprocess(self, code):
        """
        Called by preproc after the file has been parsed and all plugins called.

        In this routine, the images are produced in bulk

        Code string is not modified
        """
        for f in self.jobs.keys():
            jobs = self.jobs[f]
            #omnigraffle_export.export(grafflefile, imgname, canvasname=canvasname)
            # applescript alternative seems better, it's faster and background:
            self.export_graffle(f, jobs)

        return code

# hacked this up, I really have no idea how to actually figure out what capabilities
# exist within applescript. Yay to the internet.
# http://www.leancrew.com/all-this/2013/03/combining-python-and-applescript/
# http://forums.omnigroup.com/showthread.php?t=24079
graffle_export_script = """
tell application "OmniGraffle"
  set area type of current export settings to all graphics
  open "%s"
  set theDocument to front document
  %s
  close front document
end tell
"""

# This is the template for exporting  canvas.  It will be inserted in the script 1 or
# more times.
graffle_export_canvas = """
  set canvas of front window to canvas "%s" of theDocument
  tell front document to save in file "%s"
"""
  
def macpath(fname):
    return os.path.abspath(fname).replace("/", ":").lstrip(":")


new = GrafflePlugin
