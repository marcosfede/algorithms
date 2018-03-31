Problem
You are about to host a fashion show to show off three new styles of clothing. The show will be held on a stage which is in the most fashionable of all shapes: an N-by-N grid of cells.

Each cell in the grid can be empty (which we represent with a . character) or can contain one fashion model. The models come in three types, depending on the clothing style they are wearing: +, x, and the super-trendy o. A cell with a + or x model in it adds 1 style point to the show. A cell with an o model in it adds 2 style points. Empty cells add no style points.

To achieve the maximum artistic effect, there are rules on how models can be placed relative to each other.

Whenever any two models share a row or column, at least one of the two must be a +.
Whenever any two models share a diagonal of the grid, at least one of the two must be an x.
Formally, a model located in row i0 and column j0 and a model located in row i1 and column j1 share a row if and only if i0 = i1, they share a column if and only if j0 = j1, and they share a diagonal if and only if i0 + j0 = i1 + j1 or i0 - j0 = i1 - j1.

For example, the following grid is not legal:

...
x+o
.+.
The middle row has a pair of models (x and o) that does not include a +. The diagonal starting at the + in the bottom row and running up to the o in the middle row has two models, and neither of them is an x.

However, the following grid is legal. No row, column, or diagonal violates the rules.

+.x
+x+
o..
Your artistic advisor has already placed M models in certain cells, following these rules. You are free to place any number (including zero) of additional models of whichever types you like. You may not remove existing models, but you may upgrade as many existing + and x models into o models as you wish, as long as the above rules are not violated.

Your task is to find a legal way of placing and/or upgrading models that earns the maximum possible number of style points.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with one line with two integers N and M, as described above. Then, M more lines follow; the i-th of these lines has a +, x, or o character (the type of the model) and two integers Ri and Ci (the position of the model). The rows of the grid are numbered 1 through N, from top to bottom. The columns of the grid are numbered 1 through N, from left to right.

Output
For each test case, first output one line containing Case #x: y z, where x is the test case number (starting from 1), y is the number of style points earned in your arrangement, and z is the total number of models you have added and/or substituted in. Then, for each model that you have added or substituted in, output exactly one line in exactly the same format described in the Input section, where the character is the type of the model that you have added or substituted in. These z lines can be in any order.

If there are multiple valid answers, you may output any one of them.

Limits
1 ≤ T ≤ 100.
1 ≤ N ≤ 100.
1 ≤ Ci ≤ N, for all i.
0 ≤ M ≤ N2.
No two pre-placed models appear in the same cell.
It is guaranteed that the set of pre-placed models follows the rules.
Small dataset
Ri = 1, for all i. (Any models that are pre-placed are in the top row. Note that you may add/replace models in that row and/or add models in other rows.)
Large dataset
1 ≤ Ri ≤ N, for all i.
Sample

Input 
 	
Output 
 
3
2 0
1 1
o 1 1
3 4
+ 2 3
+ 2 1
x 3 1
+ 2 2

Case #1: 4 3
o 2 2
+ 2 1
x 1 1
Case #2: 2 0
Case #3: 6 2
o 2 3
x 1 2

The sample output displays one set of answers to the sample cases. Other answers may be possible. Note that the last sample case would not appear in the Small dataset.

In sample case #1, the grid is 2-by-2 and is initially blank. The output corresponds to the following grid. (In these explanations, we will use . to denote a blank cell.)

x.
+o
In sample case #2, the only cell is already occupied by an o model, and it is impossible to add a new model or replace the o model.

In sample case #3, the grid looks like this before you place any models:

...
+++
x..
The output corresponds to this grid:

.x.
++o
x..



# Analysis

Fashion Show: Analysis
What's really going on here?
The somewhat strange scenario presented in this problem disguises a classic type of chess problem in which pieces must be placed so that they do not attack each other. The eight queens puzzle is one well-known example. Our problem is more complicated, and it involves three types of piece. Let's restate the rules about how the models can interact in more chess-like terms:

The + models are bishops. Two bishops may not occupy the same diagonal.
The x models are rooks. Two rooks may not occupy the same row or column.
The o pieces are queens. Two queens may not occupy the same row, column, or diagonal. Moreover, a queen and a bishop may not occupy the same diagonal; a queen and a rook may not occupy the same row or column.
Observe that our problem does not accord with typical chess rules about "attacks". For example, in our problem, it is fine for a rook and a bishop to share the same row or column. Also, unlike in chess, a piece between two pieces does not prevent them from "attacking" each other. For example, we do not allow two bishops to share the same diagonal even if there is a rook between them.

Decomposing the problem
How will we deal with this variety of pieces? The critical insight is that the rook and bishop parts of the problem are independent; we can solve them separately, placing as many new pieces in each subproblem as possible, and then merge the answers together. A queen is just a rook plus a bishop; we can add each pre-placed queen into the rook subproblems as a rook and into the bishop subproblem as a bishop. Then, once the subproblems are solved, we can turn any cell that is occupied in both subproblem solutions back into a queen.

This strategy is guaranteed not to violate any rules. A rook subproblem solution will never have two rooks in the same row or column, and a bishop subproblem solution will never have two bishops on the same diagonal. Merging the two subproblems' solutions may generate new queens, but it is impossible for them to violate any rules, since that would imply a rule violation in one of the subproblems. For example, we do not need to worry that we will end up with a queen and a bishop on the same diagonal, since that would only be possible if our bishop solution had two bishops on the same diagonal.

Moreover, as long as we place as many rooks as possible in the rook subproblem, and as many bishops as possible in the bishop subproblem, we are guaranteed the maximum possible amount of style points for our test case. Since queens are worth 2 points, merging a rook and a bishop into a queen has no effect on our score.

Let's walk through an example. This case:

+..
+.o
x..
can be decomposed into rook and bishop problems:

... +..
..x +.+
x.. ...
which can be solved independently:

.x. +..
..x +.+
x.. +..
and then merged back together. Note that we have replaced the former x model from the lower left corner with an o model.

+x.
+.o
o..
Solving the subproblems
Now all we need are strategies for the subproblems themselves. The rook problem is straightforward. Each rook removes exactly one row and column from further consideration, so any greedy placement strategy that does not violate the rules will place exactly N rooks.

The bishop subproblem is more challenging. We can approach it differently in the Small and Large datasets.

Bishops: Small dataset
In the Small dataset, any pre-placed pieces are all in the top row. Observe that bishops in the same row or column cannot possibly "threaten" each other, and so we can safely add a bishop to any top row cell that does not already have one. So, if we can come up with a general solution pattern in which the top row is always completely filled with bishops, then we can solve any Small test case, because we can safely turn any pre-placed arrangement into a row packed with bishops.

Once the top row is filled with bishops, where else on the board should we put them? The bottom row is farthest away from the constraints imposed by the top row, and we can try putting a bishop in every bottom-row cell except for the cells on either end (which are "threatened" by the bishops at the two ends of the top row). These bishops do not threaten each other or any top row bishops, so this arrangement is valid, and we have a total of 2N-2 bishops. No additional bishops can be added after that, though. Have we really placed as many as possible?

At this point, we can experiment and convince ourselves that this solution is probably optimal. We can also take a leap of faith; for a Small dataset in a Qualification Round, there is little incentive not to submit the solution and see if it is correct. Or, we can come up with a proof. An N by N board has 4N-2 different diagonals. Moreover, the parallel diagonals of length 1 in opposite corner cells can never both be used simultaneously, so there are really only 4N-4 simultaneously usable diagonals. Since placing a bishop uses up two diagonals, 2N-2 is an upper bound on the number of bishops we can place. So, our method is optimal!

We must still take care, though, to handle a pre-placed rook/queen correctly if one is present, and to merge the rook and bishop solutions appropriately, creating queens when necessary. We must also be careful with the 1 by 1 board, which has no bottom row distinct from its top row.

It is possible to come up with the same construction without realizing that the problem can be decomposed into rooks and bishops; it is just more difficult to justify the optimality of the construction in that case!

Bishops: Large dataset
One helpful observation is that, just as in a chess game, the "white cell" bishops (in our problem, cells for which Ri + Ci is even) are completely independent of the "black cell" bishops (cells for which that sum is odd). So we can consider these as sub-sub-problems.

You can use a bipartite matching algorithm to place the bishops optimally. There is, however, a greedy strategy; unlike in the rook subproblem, however, not just any greedy strategy will work!

Let's consider an 8 x 8 board with no pre-placed bishops. We'll look at just the "black" cells of the board, and tilt the board 45 degrees clockwise. (Here, .s represent black cells. The @s do not represent cells — they are just there to orient the image.)

@@@..@@@
@@....@@
@......@
........
@......@
@@....@@
@@@..@@@
This new board has an important property: any row is a subset of all rows with more black cells than it. For example, the four black cells in the second row are also present in every row with at least four black cells. This property holds regardless of the value of N, or whether we look at "white" or "black" cells. It even holds as we add bishops! Adding a bishop wipes out one entire row and one entire column — notice that we have made this more like the rook problem — and since the remaining rows have all lost the same column, the aforementioned property is unchanged.

The property suggests a greedy strategy: first, sort the rows by the number of available cells. Then, pick a "smallest" row (one with a minimal number of available cells), place a bishop in any column in that row, and wipe out that row and column. This strategy is guaranteed to place an optimally large number of bishops. Suppose that we choose a column C in the smallest row R, and another column C' in some other row R', such that C' is also in R. Then C must also be in R', since all columns in the smallest row are in every other row. We can therefore swap them over, and it is equally valid to choose C' in row R and C in row R'.

One tempting (but incorrect) greedy strategy is to go left to right, top to bottom, and greedily place bishops in all legal places. Here is an example of a board for which that fails.

.@@@@
....@
...@@
..@@@
.@@@@
The incorrect greedy strategy will only place three bishops, as follows:

+@@@@
.+..@
..+@@
..@@@
.@@@@
whereas the correct strategy will place four (here is one optimal placement):

.@@@@
...+@
..+@@
.+@@@
+@@@@
Notice that although we can always place N rooks, the number of bishops we are able to place depends on the pre-placed bishops. This explains why different test cases with the same value of N might have different maximum scores.
