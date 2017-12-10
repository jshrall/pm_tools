
---
title: Comma and Tab Separated Tables
...

# CSV and TSV tables

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

