
---
title: Schematic Diagrams
...

# Schematic Diagram

For drawing circuit diagrams with the aid of [ShemDraw](https://bitbucket.org/cdelker/schemdraw),
the following syntax can be used:

`schemdraw("Diagram title")`

For example, the below code:

```python
d.add(e.GND)
d.add(e.SOURCE_V, label='$V_{OUT}$')
d.add(e.RES, label='$R_{AVP}$')
d.add(e.DOT); d.push()
rl1 = d.add(e.RES, d='up')
d.labelI(rl1, '$I_{load1}$')
d.pop()
rpp = d.add(e.RES)
rpp.add_label('$R_{pp}$', loc='bot')
d.labelI(rpp, '$I_{CROSS}$')
d.add(e.DOT); d.push()
rl2 = d.add(e.RES, d='up')
d.labelI(rl2, '$I_{load2}$', top=False)
d.pop()
d.add(e.RES, botlabel='$R_{AVP}$', d='down')
d.add(e.SOURCE_V, botlabel='$V_{OUT}+V_{ERR}$', reverse=True, d='down')
d.add(e.GND)
```

Is rendered into this schematic diagram:

```schemdraw("Supply cross-current simulation")
d.add(e.GND)
d.add(e.SOURCE_V, label='$V_{OUT}$')
d.add(e.RES, label='$R_{AVP}$')
d.add(e.DOT); d.push()
rl1 = d.add(e.RES, d='up')
d.labelI(rl1, '$I_{load1}$')
d.pop()
rpp = d.add(e.RES)
rpp.add_label('$R_{pp}$', loc='bot')
d.labelI(rpp, '$I_{CROSS}$')
d.add(e.DOT); d.push()
rl2 = d.add(e.RES, d='up')
d.labelI(rl2, '$I_{load2}$', top=False)
d.pop()
d.add(e.RES, botlabel='$R_{AVP}$', d='down')
d.add(e.SOURCE_V, botlabel='$V_{OUT}+V_{ERR}$', reverse=True, d='down')
d.add(e.GND)
```

Documentation for the syntax can be found at <https://cdelker.bitbucket.io/SchemDraw/SchemDraw.html>.

Under the hood, user-provided code is inserted in the following template
and executed as a regular python program:

```python
import SchemDraw as schem
import SchemDraw.elements as e
import SchemDraw.logic as l
d = schem.Drawing()
# ...
# Your code goes here
# ...
d.draw(showplot=False)
d.save("<image file name>")
```
