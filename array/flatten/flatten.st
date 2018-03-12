#(2 1 #(3 #(4 5) 6) 7 #(8)) flattened.

" Note that the flattened method is part of the std image of Pharo. 
  Another possible solution could be: "

Object >> flat
	^ {self}
  
Collection >> flat
	^ self flatCollect: [ :each | each flat ]
  
#(2 1 #(3 #(4 5) 6) 7 #(8)) flat.
