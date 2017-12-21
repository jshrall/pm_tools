
---
title: Ascii Art Plugin
...

# Diagrams Through Ascii Art (ditaa)

You can embedded diagrams written in ASCII Art using ditaa. The syntax spec for ditaa can be found at [ditaa website](http://ditaa.sourceforge.net)

Here is an example of a diagram using ditaa.

<pre><code>&#96;&#96;&#96;ditaa("Block Diagram")
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
&#96;&#96;&#96;
</code></pre>

Will create the following diagram:

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

# Signal Interfaces

Using the simple syntax provided below, you can develop some simple but effective diagrams to
describe signal interfaces between two logic blocks.  This plugin is called `sigint`.

Syntax is as follows.  The 'clock' and 'power' tags are special.  They are detected by looking for
the exact syntax as show below.  If found, they will be picked up and placed in the summary table.

<pre><code>&#96;&#96;&#96;sigint("Test Interface")
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
&#96;&#96;&#96;
</code></pre>


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
