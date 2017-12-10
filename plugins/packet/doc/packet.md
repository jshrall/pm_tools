---
title: Packet Plugin
...

# Packet Definitions

Also supported are packet data types.  These are essentially the same as 
registers but with a visual picture of the bits.

### Simple Packets

```packet("Trace Packet", 31)
14:0  | Clock Counts | Total clock count so far
22:16 | Reserved     | Reserved
36:24 | Split Field  | This field is split across words
41:38 | Idle Timer   | Time spent idle
42:43 | Super Short Field Name   | This is a single bit field with a long name
62:44 | Reserved     | 
```

