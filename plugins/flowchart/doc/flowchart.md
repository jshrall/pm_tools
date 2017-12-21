
---
title: Flow Chart Plugin
...

# Flow Chart diagrams

Flow charts can be embedded as follows. Syntax and examples can be found at <http://flowchart.js.org>.

**Source**:

<pre><code>
&#96;&#96;&#96;flowchart("Flowchart Diagram Example")
st=>start: Start
e=>end
op1=>operation: My Operation
sub1=>subroutine: My Subroutine
cond=>condition: Yes
or No?
io=>inputoutput: catch something...

st->op1->cond
cond(yes)->io->e
cond(no)->sub1(right)->op1
&#96;&#96;&#96;
</code></pre>

**Rendered**:

```flowchart("Flowchart Diagram Example")
st=>start: Start
e=>end
op1=>operation: My Operation
sub1=>subroutine: My Subroutine
cond=>condition: Yes
or No?
io=>inputoutput: catch something...

st->op1->cond
cond(yes)->io->e
cond(no)->sub1(right)->op1
```

Links in the diagrams are not enabled at the moment, as they are overridden by the zoom
functionality.


