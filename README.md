# Overview

**pm_tools** is a framework for authoring technical documentation in markdown. Basic markdown
capabilities are provided by pandoc. Pm_tools extends pandoc-flavored markdown with "plugin" syntax
that allows embedding:

* [Plantuml](http://plantuml.com) diagrams
* [Graphviz](http://www.graphviz.org) charts
* [Wavedrom](http://wavedrom.com) waveform diagrams
* [Ditaa](http://ditaa.sourceforge.net) diagrams
* [Flowchart.js](http://flowchart.js.org) diagrams
* [Schemdraw](https://cdelker.bitbucket.io/SchemDraw/SchemDraw.html) circuit diagrams
* [Mathjax](https://www.mathjax.org) formulas
* [Mermaid](https://mermaidjs.github.io) diagrams
* Arbitrary python code output
* Data structure (registers, packets) definitions
* Omnigraffle diagrams (as zoomable SVG)
* Excel tables (as HTML tables)
* csv/tsv/psv
* Integrated glossary

Main output format is HTML (single-file), with PDF also supported.

Principles of pm_doc:

* Ability to edit documents fully offline
* Ability to view documents fully offline (Mathjax formulas currently require online connection or
  cached Mathjax)
* Single, self-contained output document contained in a single HTML file (to make easy to copy / send by e-mail)

# Requirements

* Python 2.7

# Quick start

Create a file named `hello.md` with the following content:

    # Quick start example

    ## Hello, World

    ```plantuml("Communication to the world")
    Pm_doc -> World: Hello there
    ```

Run from the git bash (recommended) console:

    python $PM_DOC/scripts/mmd2doc.py hello.md

Above command should produce hello.html file similar to
[this](https://jshrall.github.io/pm_tools/doc/hello_world/hello.html).

# Next steps

An overview of all features with the examples can be found here:

[example.html](https://jshrall.github.io/pm_tools/doc/example.html). The source of this document
is in [doc/example.md](https://jshrall.github.io/pm_tools/doc/example.md) and the plugin source
docs are all in [plugins/\*/doc/\*.md](https://jshrall.github.io/pm_tools/plugins/doc). The best
way to learn pm_tools features is to display sourc markdown and output
[example.html](https://jshrall.github.io/pm_tools/doc/example.html) side-by-side and compare.

Note: PM_TOOLS rendering of the [README.md](README.md) you are reading right now can be viewed here:
[README.html](https://jshrall.github.io/pm_tools/README.html).

# FIXME

The following features are missing from this **pm_doc** distribution:

* Test/regressions
* Build/release automation
* Python 3 support