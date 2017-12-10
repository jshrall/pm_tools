
---
title: Excel Image Snapshot Plugin
...

# Excel Image Snapshot

<mark>Currently unsupported</mark>

Ranges of cells from excel files can be embedded as pictures to preserve exact appearance as when
viewed in Excel application.

Command Syntax:

`xlsimg("filename.xlsx" [, sheet="Sheet name (optional)"] [, range="Range (optional)"] [, title="Title Override (optional)"])`

Arguments:

* "Sheet name (optional)" - specifies sheet name to snapshot. If not supplied or equals "" and range
  doesn't specify the page either, first sheet will be selected.
* "Range (optional)" - Excel range to snapshot. Syntax is whatever Excel allows - see examples
  below. If not supplied or equals "", all used cells in a sheet are selected.
* "Title Override (optional)" - when supplied, will be used when displaying the table instead of the
  sheet name.

Example syntax:

`xlsimg("test.xlsx", title="MyTitle")`

`xlsimg("test.xlsx", sheet="Sheet2", title="The Title")`

`xlsimg("test.xlsx", range="MyNamedRange")`

`xlsimg("test.xlsx", range="Sheet3!B5:C8")`

`xlsimg("test.xlsx", range="Sheet4!SheetScopedNamedRange")`

Usage example:

`xlsimg("pm_doc_demo.xlsx", range="SquaresAndCubes", title="Squares and Cubes")`

FIXME 

`xlsimg("pm_doc_demo.xlsx", range="SquaresAndCubes", title="Squares and Cubes")
`

