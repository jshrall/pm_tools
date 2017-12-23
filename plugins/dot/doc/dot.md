
---
title: Dot / Graphviz Plugin
...

# DOT / Graphviz

You can integrate dot diagrams as follows.  The syntax spec for dot graphs can be found at 
[graphviz.org](http://www.graphviz.org).
 
The following example code:

<pre><code>&#96;&#96;&#96;dot("Sample Flowchart"){width:600px}
digraph { 

  rankdir=LR;

  "low-priority" [shape="doublecircle" color="cornflowerblue"];
  "high-priority" [shape="doublecircle" color="cornflowerblue"];

  "s1" -> "low-priority";
  "s2" -> "low-priority";
  "s3" -> "low-priority";

  "low-priority" -> "s4";
  "low-priority" -> "s5";
  "low-priority" -> "high-priority" [label="wait-time exceeded"];

  "high-priority" -> "s4";
  "high-priority" -> "s5";

}
&#96;&#96;&#96;
</code></pre>

Generates this picture:

```dot("Sample Flowchart"){width:600px}
digraph { 

  rankdir=LR;

  "low-priority" [shape="doublecircle" color="cornflowerblue"];
  "high-priority" [shape="doublecircle" color="cornflowerblue"];

  "s1" -> "low-priority";
  "s2" -> "low-priority";
  "s3" -> "low-priority";

  "low-priority" -> "s4";
  "low-priority" -> "s5";
  "low-priority" -> "high-priority" [label="wait-time exceeded"];

  "high-priority" -> "s4";
  "high-priority" -> "s5";
}

```

Below is a large diagram that is too small to see. Using the native zoom/pan features of the SVG you 
can inspect all of the low level details. The source of the graph came from the [graphviz example 
site](https://graphviz.gitlab.io/_pages/Gallery/directed/profile.html).

```dot("Unix"){max-width: 400px}
digraph unix {
	size="6,6";
	node [color=lightblue2, style=filled];
	"5th Edition" -> "6th Edition";
	"5th Edition" -> "PWB 1.0";
	"6th Edition" -> "LSX";
	"6th Edition" -> "1 BSD";
	"6th Edition" -> "Mini Unix";
	"6th Edition" -> "Wollongong";
	"6th Edition" -> "Interdata";
	"Interdata" -> "Unix/TS 3.0";
	"Interdata" -> "PWB 2.0";
	"Interdata" -> "7th Edition";
	"7th Edition" -> "8th Edition";
	"7th Edition" -> "32V";
	"7th Edition" -> "V7M";
	"7th Edition" -> "Ultrix-11";
	"7th Edition" -> "Xenix";
	"7th Edition" -> "UniPlus+";
	"V7M" -> "Ultrix-11";
	"8th Edition" -> "9th Edition";
	"1 BSD" -> "2 BSD";
	"2 BSD" -> "2.8 BSD";
	"2.8 BSD" -> "Ultrix-11";
	"2.8 BSD" -> "2.9 BSD";
	"32V" -> "3 BSD";
	"3 BSD" -> "4 BSD";
	"4 BSD" -> "4.1 BSD";
	"4.1 BSD" -> "4.2 BSD";
	"4.1 BSD" -> "2.8 BSD";
	"4.1 BSD" -> "8th Edition";
	"4.2 BSD" -> "4.3 BSD";
	"4.2 BSD" -> "Ultrix-32";
	"PWB 1.0" -> "PWB 1.2";
	"PWB 1.0" -> "USG 1.0";
	"PWB 1.2" -> "PWB 2.0";
	"USG 1.0" -> "CB Unix 1";
	"USG 1.0" -> "USG 2.0";
	"CB Unix 1" -> "CB Unix 2";
	"CB Unix 2" -> "CB Unix 3";
	"CB Unix 3" -> "Unix/TS++";
	"CB Unix 3" -> "PDP-11 Sys V";
	"USG 2.0" -> "USG 3.0";
	"USG 3.0" -> "Unix/TS 3.0";
	"PWB 2.0" -> "Unix/TS 3.0";
	"Unix/TS 1.0" -> "Unix/TS 3.0";
	"Unix/TS 3.0" -> "TS 4.0";
	"Unix/TS++" -> "TS 4.0";
	"CB Unix 3" -> "TS 4.0";
	"TS 4.0" -> "System V.0";
	"System V.0" -> "System V.2";
	"System V.2" -> "System V.3";
}
```
