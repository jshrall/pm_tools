import os

class MermaidPlugin(object):

    def __init__(self, preprocessor):
        self.mermaid_js = preprocessor.toolpath("plugins/mermaid/mermaid.cli/index.bundle.js")
        # Config and style are both currently unused
        #self.mermaid_cfg = preprocessor.toolpath("plugins/mermaid/mermaid_config.json")
        #self.mermaid_css = preprocessor.toolpath("plugins/mermaid/mermaid.css")
        self.pp = preprocessor
        self.token = "mermaid"
        self.pp.register_plugin(self)

    def process(self, code, filename_or_title, title=None, div_style=None):
        """
        Process mermaid code and return the proper insertion string
        """

        mmdfile, outfile, update, title = self.pp.get_source(code, filename_or_title, ".mmd", ".svg", title)

        if update:
            self.mermaid2img(mmdfile, outfile)

        return self.pp.img2md(outfile, title, div_style)

    def mermaid2img(self, infile, outfile):
        """Convert mermaid file to image output file.
        
        Args:
            infile (str): [description]
            outfile (str, optional): Defaults to None. Image will be written to this file. The outfile extension describes the type,
                either png or svg.
        """

        try:
            if outfile and os.path.exists(outfile):
                os.unlink(outfile)
            self.pp._call(r'"%s" -i "%s" -o "%s"' % (self.mermaid_js, infile, outfile))
        except SystemExit:
            # If mermaid failed, but generated output SVG, that SVG contains error description
            # so should be good enough to continue
            if outfile and os.path.exists(outfile):
                print "Ignoring the error above. See mermaid output diagram for detailed error description"
            else:
                raise

new = MermaidPlugin
