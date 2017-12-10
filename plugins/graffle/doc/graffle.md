---
title: Graffle
...

# Graffle Diagrams

Graffle diagrams may be inserted using the following syntax:

<pre><code>&#96;&#96;&#96;graffle("assets/file.graffle", "Canvas Name", "Optional Title")  
&#96;&#96;&#96;</code></pre>

Below is an example insertion of the document:

```graffle("assets/sample.graffle", "Canvas 1", "Sample Graffle Diagram")
```

If no name is supplied, the name of the canvas in the file is used:

<pre><code>&#96;&#96;&#96;graffle("assets/sample.graffle", "Canvas 1")  
&#96;&#96;&#96;</code></pre>

```graffle("assets/sample.graffle", "Canvas 1")
```

If there is a document with multiple canvasses, it is possible to insert them individually.

<pre><code>&#96;&#96;&#96;graffle("assets/sample.graffle", "Second Canvas")  
&#96;&#96;&#96;</code></pre>

```graffle("assets/sample.graffle", "Second Canvas")
```

Finally, below is an example of a larger picture that has been forcibly resized to be smaller.

<pre><code>&#96;&#96;&#96;graffle("assets/sample.graffle", "Complex"){max-width: 400px}
&#96;&#96;&#96;</code></pre>

```graffle("assets/sample.graffle", "Complex"){max-width: 400px}
```
