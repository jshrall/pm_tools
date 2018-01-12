
---
title: Comma and Tab Separated Tables
...

# Comma, Tab and Pipe Tables

You can edit a table in excel, save as CSV, and use the csv import widget to import it into the final output.
If the code block is empty, it will automatically look for a file to fill it.

```csv("assets\survey.csv", "Mental Health in Tech survey")
```

You can also do a simple csv in text format using commas as a delimiter.

Commas in the data are accepted if they are escaped, '\\,'.

```csv("Simple Table")
Day, High Temperature, Low Temperature
Monday, 65, 49
Tuesday, 63, 42
Wednesday, 72, 45
Funday, 72, 45\,46
```

Tab separated lists are also supported using the 'tsv' tag.  For example.

```tsv("US States (plus Washington D.C.) Population and Ranking")
State	Population Ranking	Population Census Data: 2013
District of Columbia	49	646,449
Vermont	50	626,630
Wyoming	51	582,658
```

Pipe (|) separated lists are also supported using the '|' tag.  For example.

```psv("US States (plus Washington D.C.) Population and Ranking")
State | Population Ranking | Population Census Data: 2013
District of Columbia | 49 | 646,449
Vermont | 50 | 626,630
Wyoming | 51 | 582,658
```

Visually, it can help to have a separator between the first header row and the rest. This will be 
ignored. `---` or `===` may be used as a separator

```
State                | Population Ranking | Population Census Data: 2013
========================================================================
District of Columbia | 49                 | 646,449
Vermont              | 50                 | 626,630
Wyoming              | 51                 | 582,658
```

Finally, for custom column separators, you can call the library like this:

`csv("Title", separator="X")`

