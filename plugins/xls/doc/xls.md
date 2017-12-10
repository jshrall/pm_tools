
---
title: Excel Reader Plugin
...

# Excel Tables

This formatting:

<pre><code>&#96;&#96;&#96;xls("assets\pm_doc_demo.xlsx", "Sheet name" [, "Title Override (optional)"])  
&#96;&#96;&#96;</code></pre>

Tells the tools to open pm_doc_demo.xlsx, grab the sheet ID named 'Sheet name', and insert its 
contents into the document. It will also automatically link the table to the original XLSX for 
further detailed review. If the optional title override is supplied, it will be used when displaying 
the table instead of the actual sheet name.

```xls("assets\pm_doc_demo.xlsx", "Project Tracker", "Sample Excel Sheet")
```

## Footnotes

Footnotes may be added automatically to the spreadsheet by inserting comments in the cell in which 
you want a footnote attached.  For example, see below a few footnotes automatically inserted from 
the excel spreadsheet's comments.  Cross-reference hyperlinks are also included for easy navigation.

```xls("assets\pm_doc_demo.xlsx", "Invoices")
```

## Colors

You can integrate colors into the cells and they will be rendered in the output. Coloring of 
individual words within a cell is not supported.

```xls("assets/sample.xlsx", "colors")
```

## Cell Merging and Rotation

Merged and rotated cells are all supported, see as follows

```xls("assets/sample.xlsx", "merge")
```

