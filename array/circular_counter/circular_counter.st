circ_counter := [ :array :skip |
	| index |
	index := 1.
	[array size > 0] whileTrue: [ 
		index := (skip + index - 2 % array size) + 1.
		Transcript show: (array removeAt: index)]
].

a := #(1 2 3 4 5 6 7 8 9) asOrderedCollection.

circ_counter value: a value: 3.
