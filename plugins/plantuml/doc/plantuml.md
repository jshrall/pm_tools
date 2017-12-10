
---
title: Plantuml Plugin
...

# Plantuml 

Below is embedded plantuml sequence diagram.  The syntax spec for plantuml can be found at
[plantuml.com](http://www.plantuml.com).

```plantuml("Conversation between Alice and Bob")
Alice->Bob : hello
note left: this is a first note

Bob->Alice : ok
note right: this is another note

Bob->Bob : I am thinking
note left
	a note
	can also be defined
	on several lines
end note
```

