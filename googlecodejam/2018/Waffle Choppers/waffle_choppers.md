Waffle Choppers
Problem
The diners at the Infinite House of Pancakes have gotten tired of circular pancakes, so the chefs are about to offer a new menu option: waffles! As a publicity stunt, they have made one large waffle that is a grid of square cells with R rows and C columns. Each cell of the waffle is either empty, or contains a single chocolate chip.

Now it is time for the chefs to divide up the waffle among their hungry diners. A horizontal cut runs along the entire gridline between two of the rows; a vertical cut runs along the entire gridline between two of the columns. For efficiency's sake, one chef will make exactly H different horizontal cuts and another chef will make exactly V different vertical cuts. This will conveniently create one piece for each of the (H + 1) × (V + 1) diners. The pieces will not necessarily all be of equal sizes, but that is fine; market research has shown that the diners do not care about that.

What the diners do care about is the number of chocolate chips they get, so each piece must have exactly the same number of chocolate chips. Can you determine whether the chefs can accomplish this goal using the given numbers of horizontal and vertical cuts?

Input
The first line of the input gives the number of test cases, T; T test cases follow. Each begins with one line containing four integers R, C, H, and V: the number of rows and columns in the waffle, and the exact numbers of horizontal and vertical cuts that the chefs must make. Then, there are R more lines of C characters each; the j-th character in the i-th of these lines represents the cell in the i-th row and the j-th column of the waffle. Each character is either @, which means the cell has a chocolate chip, or ., which means the cell is empty.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is POSSIBLE if the chefs can accomplish the goal as described above, or IMPOSSIBLE if they cannot.

Limits
1 ≤ T ≤ 100.
Time limit: 6 seconds per test set.
Memory limit: 1GB.

Test set 1 (Visible)
2 ≤ R ≤ 10.
2 ≤ C ≤ 10.
H = 1.
V = 1.

Test set 2 (Hidden)
2 ≤ R ≤ 100.
2 ≤ C ≤ 100.
1 ≤ H < R.
1 ≤ V < C.

Sample

Input 
 	
Output 
 
6
3 6 1 1
.@@..@
.....@
@.@.@@
4 3 1 1
@@@
@.@
@.@
@@@
4 5 1 1
.....
.....
.....
.....
4 4 1 1
..@@
..@@
@@..
@@..
3 4 2 2
@.@@
@@.@
@.@@
3 4 1 2
.@.@
@.@.
.@.@

Case #1: POSSIBLE
Case #2: IMPOSSIBLE
Case #3: POSSIBLE
Case #4: IMPOSSIBLE
Case #5: POSSIBLE
Case #6: IMPOSSIBLE

Note that the last two sample cases would not appear in test set 1.

In Sample Case #1, one possible strategy is to make the horizontal cut between the second and third rows from the top, and make the vertical cut between the fourth and fifth columns from the left. That creates the following pieces, each of which has exactly two chocolate chips:

.@@. .@
.... .@

@.@. @@

In Sample Case #2, no matter where you make the horizontal cut and the vertical cut, you will create pieces with unequal numbers of chocolate chips, so the case is impossible.

In Sample Case #3, there are no chocolate chips in the waffle. Any cutting strategy creates pieces which have the same number of chocolate chips (zero), so the diners are happy... but maybe not as happy as they would have been if they had gotten chocolate chips!

In Sample Case #4, just as in Sample Case #2, you cannot succeed regardless of where you make your horizontal cut and your vertical cut.

In Sample Case #5, the chefs can make the only two possible horizontal cuts, and make the two vertical cuts to the right of the first and third columns.

Although Sample Case #6 would be possible for other numbers of horizontal and vertical cuts, remember that you must use exactly H horizontal cuts and exactly V vertical cuts. No matter where you make your one horizontal cut and two vertical cuts, you cannot succeed.
