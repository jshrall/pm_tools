
---
title: Register Definition Plugin
...

# Register Definitions

## Simple Register Format

The simple register format follows a simple scheme as follows:

```
msb:lsb | field name | Description
msb:lsb | field name | Description
...
msb:lsb | field name | Description
```

And when you are done, it will produce a format like this
```simplereg("REGNAME")
23:16 | Reserved     | Reserved
15:0  | Clock Counts | Total clock count so far
31:24 | Idle Timer   | Time spent idle
```

## Rich Register Format

Rich registers allow for things like markdown in the individual cells (multi-line descriptions) and
enumerations.

Format for rich registers is as follows.  Note that access type and reset default are optional
parameters

```
---
Attribute1: Value
Attribute2: Value
...

== MSB:LSB | Field Name | Access Type | Reset Default
Description
Multi-line is OK.
Markdown is OK.

= 0 | Enum0
= 1 | Enum1

== MSB:LSB | Field Name | RO | 0x00
An example of a register bit that spans multiple bits (msb=lsb is also allowed)

== LSB | Field Name | RO | 0x00
An example of a register bit that has just a single bit
...
```

For example:

```register("SAMPLE_REGISTER")
---
Save On PowerDown: yes
Security Policy: Secured
Address Offset: 0x1000
Description: Sample register format. This is the global description
...

== 63:48 | Enumerated State | RW | 0x0

This field has some explicitly enumerated legal values

= 0 | Enum0
= 1 | Enum1

== 32 | OneBit | RO | 0x0
This is a single bit field

== 47:33 | Reserved | RO | 0x0

== 31:16 | Read Write | RW | 0x0
This field is read/write

* Bullet1
* Bullet2

== 15:0 | Read Only | RO | 0x1234

This field is **read-only**.  It always returns 0x1234.

```

