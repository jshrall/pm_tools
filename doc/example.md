---
title: Sample Markdown Document
...

This file was generated from the source code [here](Example.mmd).  Open in a separate window to
compare it with the rendered output.

[Markdown](https://en.wikipedia.org/wiki/Markdown) syntax used for pm_doc documentation is used
widely on the Web today. Core markdown syntax is fairly standard, however there are several flavors
of the language that allow additional features like tables, etc. The flavor of markdown used in
pm_doc is called **pandoc markdown**. Good reference for pandoc markdown syntax can be found here:
[Pandoc Markdown](http://rmarkdown.rstudio.com/authoring_pandoc_markdown.html).

# Header1
## Header2
### Header3
#### Header4
##### Header5
###### Header6

# Lists

1. First ordered list item
2. Another item
    * Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
    1. Ordered sub-list
4. And another item.

   You can have properly indented paragraphs within list items. Notice the blank line above, and the 
   leading spaces (at least one, but we'll use three here to also align the raw Markdown).

   To have a line break without a paragraph, you will need to use two trailing spaces.  
   Note that this line is separate, but within the same paragraph.  
   (This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

* Unordered list can use asterisks
- Or minuses
+ Or pluses

## Numbered List <a name="explicit_reference"/>

1. Item1
1. Item2
1. Item3
1. Item4
    * attribute
    * Attribute
1. Last Item

# Formatting text

## Highlighted text

Use simple html marking to &lt;mark&gt;<mark>highlight</mark>&lt;/mark&gt;

## Emphasized text

To *emphasize* some text, surround it with `*`s or `_`, like this:

This text is _emphasized with underscores_, and this
is *emphasized with asterisks*.

Double * or _ produces **strong emphasis**:

This is **strong emphasis** and __with underscores__.

A `*` or `_` character surrounded by spaces, or backslash-escaped, will not trigger emphasis:

This is * not emphasized *, and \*neither is this\*.

Because `_` is sometimes used inside words and identifiers, pandoc does not interpret a `_`
surrounded by alphanumeric characters as an emphasis marker. If you want to emphasize just part of a
word, use `*`:

feas*ible*, not feas*able*.

## Strikeout

This ~~is deleted text.~~

## Superscripts and subscripts

H~2~O is a liquid.  2^10^ is 1024.

# More Markdown

## Comments

Use HTML-style comments `<!-- ... -->` to exclude pieces of documentation from output.
No characters are allowed between start of line and `<!--`, as well as between `-->` and line end.
Note that commented out sections will be deleted even from inside \`\`\` ... \`\`\` blocks.

<pre><code>
&lt;!--
  ...
  commented out part
  ...
-->
</code></pre>

<!--
Actual comment.
This will not appear in the output.
-->

## Tables

Simple tables can be created using markdown syntax as described
[here](http://rmarkdown.rstudio.com/authoring_pandoc_markdown.html#tables).

  Right     Left     Center     Default
-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123
      1     1          1             1

Table:  Demonstration of simple table syntax


-------     ------ ----------   -------
     12     12        12             12
    123     123       123           123
      1     1          1              1
-------     ------ ----------   -------


| Right | Left | Default | Center |
|------:|:-----|---------|:------:|
|   12  |  12  |    12   |    12  |
|  123  |  123 |   123   |   123  |
|    1  |    1 |     1   |     1  |

  : Demonstration of pipe table syntax


-------------------------------------------------------------
 Centered   Default           Right Left
  Header    Aligned         Aligned Aligned
----------- ------- --------------- -------------------------
   First    row                12.0 Example of a row that
                                    spans multiple lines.

  Second    row                 5.0 Here's another one. Note
                                    the blank line between
                                    rows.
-------------------------------------------------------------

Table: Here's the caption. It, too, may span
multiple lines.


The alternative for markdown syntax for simple tables is [Embedded CSV and TSV tables].

[Embedded XLSX Sheet] plugin allows inserting more complex tables with formatting, cell
highlighting, column span, and so on.

## Footnotes

Pandoc[^pandoc]-style markdown footnotes[^1] are supported^[Both inlines and non-inlines].

[^pandoc]: See <https://pandoc.org>

[^1]: See <https://pandoc.org/MANUAL.html#footnotes>

## Math formulas

Markdown supports LaTeX-style syntax for rendering formulas. Good quick reference for the syntax
here:
<http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference>.
There's also excellent app to identify TeX symbols from handwriting:
<http://detexify.kirelabs.org/classify.html> - just scribble any symbol there and it will give you
couple of variant to represent it in the formula. For more info, Google "latex formulas".

To insert a formula in line with the text, surround it in `$` .. `$`, e.g.:
`$P_{total} = P_{leak} + C_{dyn} * V^2 * F$`.

The result looks like this: $P_{total} = P_{leak} + C_{dyn} * V^2 * F$.

To insert a formula centered on a separate line, surround it in `$$` .. `$$`, e.g.
`$$\sum_{n=1}^{\infty} 2^{-n} = 1$$`. Here's what the result looks like:
$$\sum_{n=1}^{\infty} 2^{-n} = 1$$ 

## Cross-References

### Section Headers

You may insert a cross reference by simply using a section header's exact text such as [Numbered List]

You can also [add an explicit reference](#explicit_reference) in case it is not uniquely named in
the document.  To set up that reference, use code like this:

```
### Numbered List <a name="explicit_reference"/>
```

### Figures and Tables

To reference uniquely named figures, use `[Figure: The Title]` syntax. For example, here's the
link to [Figure: Sample Timing Diagram].

To reference uniquely named tables, use `[Table: The Title]` syntax. For example, here's the
link to [Table: Sample Excel Sheet].

### Other Files

Use the same directory structure as is in the source directory tree. For any markdown files, replace
the link with .html instead of .mmd. Use relative paths to refer to files in other directories.

## Code Syntax Highlighting

### Python Code

```python
BOARD_SIZE = 8

def under_attack(col, queens):
    left = right = col

    for r, c in reversed(queens):
        left, right = left - 1, right + 1

        if c in (left, col, right):
            return True
    return False

def solve(n):
    if n == 0:
        return [[]]

    smaller_solutions = solve(n - 1)

    return [solution+[(n,i+1)]
        for i in xrange(BOARD_SIZE)
            for solution in smaller_solutions
                if not under_attack(i+1, solution)]
for answer in solve(BOARD_SIZE):
    print answer
```

### C code

```c
#include <stdio.h>
int main()
{
   // printf() displays the string inside quotation
   printf("C Programming");
   return 0;
}
```

Text spacer

```
text 
line 2
```

### Supported languages

Full list of languages supported for syntax highlighting:
    abc, actionscript, ada, agda, apache, asn1, asp, awk, bash, bibtex, boo, c,
    changelog, clojure, cmake, coffee, coldfusion, commonlisp, cpp, cs, css,
    curry, d, diff, djangotemplate, dockerfile, dot, doxygen, doxygenlua, dtd,
    eiffel, elixir, email, erlang, fortran, fsharp, gcc, glsl,
    gnuassembler, go, hamlet, haskell, haxe, html, idris, ini, isocpp, java,
    javadoc, javascript, json, jsp, julia, kotlin, latex, lex, lilypond,
    literatecurry, literatehaskell, llvm, lua, m4, makefile, mandoc, markdown,
    mathematica, matlab, maxima, mediawiki, metafont, mips, modelines, modula2,
    modula3, monobasic, nasm, noweb, objectivec, objectivecpp, ocaml, octave,
    opencl, pascal, perl, php, pike, postscript, prolog, pure, python, r,
    relaxng, relaxngcompact, rest, rhtml, roff, ruby, rust, scala, scheme, sci,
    sed, sgml, sql, sqlmysql, sqlpostgresql, tcl, tcsh, texinfo, verilog, vhdl,
    xml, xorg, xslt, xul, yacc, yaml, zsh

## Inline Markdown Files

For large documents, it may be useful to compose text in several chapters and then merge them
together in a master document.  The tools support this using a unique tag indicating file insertion.
This tag must be in the first column of the file (no spaces at the front of the line) and must refer
to a valid markdown file (*.md or *.mmd).  See the example below.

`[_chapter1.md]`

When this file is parsed, all section headings are adjusted so that it is nested within the current
document.  For example, if the current section heading level of this document is H3 (###), then all
H1 (#) elements and text in the included file will be modified to be H4 (####). Raw text in the
main body that is not under a heading will be inserted at the H3 level.

In many cases, when developing chapters, the user would like to put them together as isolated
documents and rely on the build tools to stitch them together. Therefore, to differentiate a
chapter from a normal document, we are using a simple underscore. If a document starts with an
underscore, it will be excluded from the builds.

The following text is inserted by the tools as a nested chapter.

[_chapter1.md]

You can also insert file located in different folder relative to the current file

`[../chapters/_chapter1.md]`

If you choose to insert a file that doesn't exist, it will just pass through as-is.  No warnings or
errors are thrown. For example, see below a non-existent file.

[_chapter2.md]

Finally, in some cases you may want to insert a chapter at the base heading level (versus inline
with the containing header). To do this:

`[!_chapter1.md]`

Which results in:

[!_chapter1.md]


# Plugins

In PM_DOC context, "plugins" term refers to extensions of the regular markdown syntax that enable
pm_doc-specific functionality, such as register descriptions, flow diagrams, embedding Visio or
Excel, and so on.

Most of the time default width/height generated by the tools for showing the plugin content works
fine. Sometimes, however the result may look nicer if a particular diagram/drawing/etc. is
constrained to a certain width. In this case, specifying max-width attribute is helpful:

    ```plugin("blah"){max-width: 600px}
    ...
    ```

The syntax for attribute specification is regular [CSS style
declaration](http://www.w3schools.com/css/css_syntax.asp). When it is specified, plugin generated
content will be put inside a `<div>` element with specified style attributes.

<!-- Insert all plugin auto-documentation as child chapters -->
[../plugins/*/doc/*.md]

## Signal Interface Definition

Using the simple syntax provided below, you can develop some simple but effective diagrams to
describe signal interfaces between two logic blocks.  This plugin is called `sigint`.

Syntax is as follows.  The 'clock' and 'power' tags are special.  They are detected by looking for
the exact syntax as show below.  If found, they will be picked up and placed in the summary table.

```
sigint("Test Interface")
== srcip <- dstip: signame1
Markdown **description**
clock: dclk
power: vccd

== srcip -> dstip: signame2

== srcip <-> dstip: signame3
clock: aclk
power: vcca
This is an *example*

1. Item1
2. Item2
```


```sigint("Test Interface")
== srcip <- dstip: signame1
Markdown **description**
clock: dclk
power: vccd

== srcip -> dstip: signame2

== srcip <-> dstip: signame3
clock: bclk
power: vccb
This is an *example*

1. Item1
2. Item2
```

## Embedded VISIO Drawing

You can embed a tab in a visio document as a standalone picture.

Hyperlinks are also supported.  They will be copied locally to the 'auto' directory and inserted
as if they are locally managed in the repo.  Note that this is just a snapshot, it will only
update on a clean rebuild.

`visio("filename", "Tab Name" [, "Title Name"][, format="png"])`

`visio("assets\sample_visio.vsdx", "Page-1", "Sample Visio Diagram (click to zoom)")
`

By default, Visio diagrams will be converted to SVG (Scalable Vector Graphics) format, which
allows to search text within the images and upscale the image without quality loss. However, for some
Visio content (like embeddings from other Office tools) Visio SVG export may fail and output
image will not be correct. In such cases user can specify format="png" switch so that
Visio diagram will be converted to raster image instead of SVG, and should display exactly like
in Visio (zoom and search ability will be lost for such diagram).

BKM: if visio diagram comes out too small, you can upscale it using `{width: N px}` syntax,
similar to one described in [Specifying max-width for plugin content], e.g.:

`visio("filename", "Tab Name"){width: 800px}`

# Footnote list

Footnotes are currently collected at the end of the document:
