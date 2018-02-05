
---
title: Wavedrom Plugin
...

# Wavedrom Timing Diagram

For drawing timing diagrams, the wavedrom tool is very handy.  See the [wavedrom help
documentation](http://wavedrom.com/tutorial.html) for proper syntax.  You may integrate a raw
wavedrom source input into the document and it will be rendered by the build tools and integrated as
a figure similar to other figures.

For example, the below code:

<pre><code>&#96;&#96;&#96;wavedrom("Sample Timing Diagram")
{ signal: [
  {    name: 'clk',   wave: 'p..Pp..P'},
  ['Master',
    ['ctrl',
      {name: 'write', wave: '01.0....'},
      {name: 'read',  wave: '0...1..0'}
    ],
    {  name: 'addr',  wave: 'x3.x4..x', data: 'A1 A2'},
    {  name: 'wdata', wave: 'x3.x....', data: 'D1'   },
  ],
  {},
  ['Slave',
    ['ctrl',
      {name: 'ack',   wave: 'x01x0.1x'},
    ],
    {  name: 'rdata', wave: 'x.....4x', data: 'Q2'},
  ]
]}
&#96;&#96;&#96;</code></pre>

Is rendered into this wavedrom output

```wavedrom("Sample Timing Diagram")
{ signal: [
  {    name: 'clk',   wave: 'p..Pp..P'},
  ['Master',
    ['ctrl',
      {name: 'write', wave: '01.0....'},
      {name: 'read',  wave: '0...1..0'}
    ],
    {  name: 'addr',  wave: 'x3.x4..x', data: 'A1 A2'},
    {  name: 'wdata', wave: 'x3.x....', data: 'D1'   },
  ],
  {},
  ['Slave',
    ['ctrl',
      {name: 'ack',   wave: 'x01x0.1x'},
    ],
    {  name: 'rdata', wave: 'x.....4x', data: 'Q2'},
  ]
]}
```

## Wave Diagram Short Syntax

The syntax is basically the same, but it avoids all of the json syntax and focuses on a single line
definition of the waveform.

The format is as follows for each signal name:

`signal name   | waveform | data value list (space separated)`

A full waveform definition would look like the following.  To get nice aligned visualizations, you
may use editor tricks.  With VIM, you can use the Tabularize plugin to nicely format the text so
that it is vertically aligned at the pipes.  Once the text has been selected using visual block
mode, you can simply type `Tabularize /|` to get it to be aligned.  You can also use visual block
mode to insert columns into the waveform for easy addition or subtraction of the sequence.
Comments are annotated with #.

Lines may be defined immediately below the signal waveform.  The parser assumes that a line with no
signal name that starts with | is a node definition.  It is required that the string length of the
line definition matches that of the signal preceding it.

Blank lines between signals are assumed to be intentional spacers

<mark>Currently not supported</mark>:

* Period and phase
* Skins

<pre><code>&#96;&#96;&#96;wavedrom("Shorthand Timing Syntax")
# Waveform
clk   | p..Pp..P
      | .a......
write | 01.0....
read  | 0...1..0
addr  | x3.x4..x  | A1 A2
      | ....b...

wdata | x3.x....  | D1
ack   | x01x0.1x
      | ......c.
rdata | x.....4x  | Q2

# Edges / Arrows
a~>b This is an edge definition
b-|>c a sharp edge

# Config
hscale: 2
&#96;&#96;&#96;</code></pre>

```wavedrom("Shorthand Timing Syntax")
# Waveform
clk   | p..Pp..P
      | .a......
write | 01.0....
read  | 0...1..0
addr  | x3.x4..x  | A1 A2
      | ....b...

wdata | x3.x....  | D1
ack   | x01x0.1x
      | ......c.
rdata | x.....4x  | Q2

# Edges / Arrows
a~>b This is an edge definition
b-|>c a sharp edge

# Config
hscale: 2
```

### Section Grouping

You can add simple section identifiers to group blocks of signals.  In the example below, we have 
`====` or `____` as markers.  You can use more if desired, e.g., `_________ Dest ___________`.


```
# Waveform
==== Source ====
clk   | p..Pp..P
      | .a......
write | 01.0....
read  | 0...1..0
addr  | x3.x4..x  | A1 A2
      | ....b...

____ Dest ____ 
wdata | x3.x....  | D1
ack   | x01x0.1x
      | ......c.
rdata | x.....4x  | Q2

# Edges / Arrows
a~>b This is an edge definition
b-|>c a sharp edge

# Config
hscale: 2
```

```wavedrom("Grouped Signals")
# Waveform
==== Source ====
clk   | p..Pp..P
      | .a......
write | 01.0....
read  | 0...1..0
addr  | x3.x4..x  | A1 A2
      | ....b...

____ Dest ____
wdata | x3.x....  | D1
ack   | x01x0.1x
      | ......c.
rdata | x.....4x  | Q2

# Edges / Arrows
a~>b This is an edge definition
b-|>c a sharp edge

# Config
hscale: 2
```


