
---
title: Ascii Art Plugin
...

# Diagrams Through Ascii Art (ditaa)

You can embedded diagrams written in ASCII Art using ditaa. The syntax spec for ditaa can be found at [ditaa website](http://ditaa.sourceforge.net)

Here is an example of a diagram using ditaa.

```ditaa("Block Diagram")
+-------------+                     +-------------+
| cRED        | CLK                 | cBLK        |
|   Block     *-------------------->|   Block     |
|     A       | RST                 |     B       |
|             *-------------------->|             |
|             | DATA_OUT            |             |
|             *-------------------->|             |
|             |                     |             |
|             | DATA_IN             |             |
|             |<--------------------*             |
| +---------+ |                     | +---------+ |
| |         | |                     | |         | |
| |  Sub    | |<--------I/F-------->| |   Sub   | |
| |  Block  | |                     | |   Block | |
| +---------+ |                     | +---------+ |
+-------------+                     +-------------+
```

