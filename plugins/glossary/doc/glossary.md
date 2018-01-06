
---
title: Glossary
...

# Glossary

Inserting a glossary of terms into a document is a common task.  One of the challenging things is 
that the terms are inserted all across the document and as a document writer you don't want to have 
to add redundant definition information regarding those terms at each place. 

Using the glossary plugin, you can define terms anywhere in the document, usually in a glossary 
section, and the plugin will do the work of post-processing the document and inserting the necessary 
hyperlinks to the terminology documentation and also will add hover over bubbles to enable the 
reader to quickly see the meaning of the term.

The glossary definition specification looks like the following. The definitions are marked by `== 
term` and below the term you can insert any markdown syntax to explain it, including pictures or 
diagrams. This call will define terms and place them into the global glossary build dictionary and 
it **will not insert the glossary inline to the existing text**.  The typical usage model is for a 
user to explicitly declare the glossary in one place in the document, at the top or the bottom. Each 
section of chapter document can append to the list of glossary terms and then the glossary can be 
appended at the end as defined in [Printing the Glossary].

The parser will find exact matches of the string. They must be preceded by a space and followed by a 
space or punctuation. The search is case-sensitive, so if the word is the first in the sentence, and 
it is declared as lower case, it may be ignored.

Supercalifragilisticexpialidocious will be ignored, but supercalifragilisticexpialidocious will be 
annotated with a definition. Jabberwocky will be defined, but jabberwocky will not.

When describing an acronym, it is useful to additionally include the expansion of that acronym. The 
syntax for this is `== acronym | expansion`. E.g., for this TLA, we will get the expansion in bold 
and the rest of the definition below.

## Defining Terms

<pre><code>&#96;&#96;&#96;glossary
== terminology

The body of terms used with a particular technical application in a subject of study, theory, 
profession, etc.

== supercalifragilisticexpialidocious

Used as a nonsense word by children to express approval or to represent the longest word in English.

== hyperlink

A link from a hypertext file or document to another location or file, typically activated by 
clicking on a highlighted word or image on the screen.

== TLA | Three Letter Acronym

Commonly used in the corporate environment, knowing this term is critical.

&#96;&#96;&#96;
</code></pre>

The glossary is then rendered as follows (i.e., *it is not rendered by default*).

```glossary
== terminology

The body of terms used with a particular technical application in a subject of study, theory, 
profession, etc.

== supercalifragilisticexpialidocious

Used as a nonsense word by children to express approval or to represent the longest word in English.

== hyperlink

A link from a hypertext file or document to another location or file, typically activated by 
clicking on a highlighted word or image on the screen.

== TLA | Three Letter Acronym

Commonly used in the corporate environment, knowing this term is critical.

```

## Printing the Glossary

As you can tell from the rendered output, this first instantiation of the glossary is not actually 
printed. To get it to print, you must explicitly request the glossary to be shown as follows. In 
this example, we have added an extra term to demonstrate how all of the glossary items are collected 
into the final output.

<pre><code>&#96;&#96;&#96;glossary(show=True)
== rendered

verb (used with object)
1.  to cause to be or become; make: to render someone helpless.
2.  to do; perform: to render a service.
3.  to furnish; provide: to render aid.
4.  to exhibit or show (obedience, attention, etc.).
5.  to present for consideration, approval, payment, action, etc., as an account.
6.  to return; to make (a payment in money, kind, or service) as by a tenant to a superior: knights rendering military service to the lord.
7.  to pay as due (a tax, tribute, etc.).

&#96;&#96;&#96;
</code></pre>

```glossary(show=True)
== Jabberwocky

1. A playful imitation of language consisting of invented, meaningless words; nonsense; gibberish.
2. An example of writing or speech consisting of or containing meaningless words.

```

## Parser Corner Cases

The following conditions are all supported:

* Jabberwocky

In parenthesis: (Jabberwocky)

Jabberwocky at the start of the line and at the end: Jabberwocky

With various punctuations: Jabberwocky, Jabberwocky! Jabberwocky. Jabberwocky? "Jabberwocky" and 
'Jabberwocky'.

Inside tables:

Term        	 Definition
----        	 ----
Jabberwocky 	 Silliness
