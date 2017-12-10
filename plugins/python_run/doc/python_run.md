
---
title: Python Run Plugin
...

# Integrated Python Scripts

The 'python_run' plugin may be used to execute python code and generate output.  The script is run
standalone in a separate executable shell and the output is captured.

For example, the following code will produce a date string when embedded inside the `python_run`
plugin block:

```python
import time
print "*%s*" % time.strftime("%B %d, %Y")
```

The result is as follows:

```python_run
import time
print "*%s*" % time.strftime("%B %d, %Y")
```

### Including source in the output

If you wish to include the source into the output documentation use `python_run(source=True)`. The
above example with `source=True` looks like this:

```python_run(source=True)
import time
print "*%s*" % time.strftime("%B %d, %Y")
```

### Options for formatting the output

By default python output will be parsed as if it was part of the original document, i.e. markdown
with all the plugin processing.

For example, here's a piece of python code that produces a table in csv form:

```python_run()
print '```csv("Squares and cubes of natural numbers")\nN^1^,N^2^,N^3^'
for x in range(10):
    print "%d,%d,%d"%(x, x*x, x*x*x)
print '```'
```

Alternatively, you may want to show python output as if python was writing to a console window,
verbatim. In this case, specify the option `output="verbatim"`. Earlier example with `source=True,
output="verbatim"` will look like follows:

```python_run(source=True, output="verbatim")
import time
print "*%s*" % time.strftime("%B %d, %Y")
```

### Explicitly naming files with python code

When using `python_run` as described above, `mmd2doc.py` creates a temporary file and executes it.
Optional argument `name` allows to name the file so that it can be subsequently used in other pieces
of python code. When `name` is provided, the code will be saved to the file under `auto/<name>.py`.
This allows, for example, to define some calculation in one piece of code which source is shown, and
then demonstrate the calculation in another piece, the source of which isn't interesting to see in
final documentation. Here's an example:


```python_run(source=True, name="divtab")
valid_ratios = [8, 10, 12, 16] # defined by divider design

def ratio2divisor(ratio_req):
    # Input: 25MHz-based ratio
    # Output: (selected divisor, selected ratio)
    ratio_in = 1600 / 25 # Divider input frequency, in 25Mhz units (a constant)
    # Select valid ratio that is equal or higher than requested
    for r in valid_ratios:
        if r >= ratio_req:
            break
    divisor = ratio_in / r # integer division
    return (divisor, r)
```

```python_run(name="div_demo")
from divtab import ratio2divisor
print '```csv("Driver ratio request mapping")\n$Ratio_{req}$,$F_{req}$,$Divisor$,$F_{actual}$,$F_{CVF}$'
for ratio_req in range(4, 19):
    (divisor, result_ratio) = ratio2divisor(ratio_req)
    # To avoid another divide, approximate result frequency
    # in 25MHz-ratio steps
    cvf_freq = 25 * result_ratio
    print "%d,%d,%d,%d,%d"%(ratio_req, ratio_req*25, divisor, 1600/divisor, cvf_freq)
print "```"
```

In this example the code that produces CSV markdown for the table is hidden from the user, but the
code that performs the calculation as well as the result table are shown.


