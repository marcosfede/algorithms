Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators (not unary) +, -, or *
between the digits so they prevuate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1****2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []



# pseudocode

O(n*4^log(n))

- calculate all combinations of the 3 operators or no operator
	- this can be done using cartesian product of the set of operations against itself n-1 times
	- or generating a n-1 length number in base 4, where the digits 0,1,2 or 3 correspond to the 3 operations or no operation
- interleave those inside the string
- calculate the operation and check against target

