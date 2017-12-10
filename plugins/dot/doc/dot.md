
---
title: Dot / Graphviz Plugin
...

# DOT / Graphviz

You can integrate dot diagrams as follows.  It's super easy.  The syntax spec for dot graphs can be
found at [graphviz.org](http://www.graphviz.org).

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

