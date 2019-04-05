Last year, the Infinite House of Pancakes introduced a new kind of pancake. It has a happy face made of chocolate chips on one side (the "happy side"), and nothing on the other side (the "blank side").

You are the head cook on duty. The pancakes are cooked in a single row over a hot surface. As part of its infinite efforts to maximize efficiency, the House has recently given you an oversized pancake flipper that flips exactly K consecutive pancakes. That is, in that range of K pancakes, it changes every happy-side pancake to a blank-side pancake, and vice versa; it does not change the left-to-right order of those pancakes.

You cannot flip fewer than K pancakes at a time with the flipper, even at the ends of the row (since there are raised borders on both sides of the cooking surface). For example, you can flip the first K pancakes, but not the first K - 1 pancakes.

Your apprentice cook, who is still learning the job, just used the old-fashioned single-pancake flipper to flip some individual pancakes and then ran to the restroom with it, right before the time when customers come to visit the kitchen. You only have the oversized pancake flipper left, and you need to use it quickly to leave all the cooking pancakes happy side up, so that the customers leave feeling happy with their visit.

Given the current state of the pancakes, calculate the minimum number of uses of the oversized pancake flipper needed to leave all pancakes happy side up, or state that there is no way to do it.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a string S and an integer K. S represents the row of pancakes: each of its characters is either + (which represents a pancake that is initially happy side up) or - (which represents a pancake that is initially blank side up).

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is either IMPOSSIBLE if there is no way to get all the pancakes happy side up, or an integer representing the the minimum number of times you will need to use the oversized pancake flipper to do it.

Limits
1 ≤ T ≤ 100.
Every character in S is either + or -.
2 ≤ K ≤ length of S.
Small dataset
2 ≤ length of S ≤ 10.
Large dataset
2 ≤ length of S ≤ 1000.
Sample

Input 
 	
Output 
 
3
---+-++- 3
+++++ 4
-+-+- 4

Case #1: 3
Case #2: 0
Case #3: IMPOSSIBLE
In Case #1, you can get all the pancakes happy side up by first flipping the leftmost 3 pancakes, getting to ++++-++-, then the rightmost 3, getting to ++++---+, and finally the 3 pancakes that remain blank side up. There are other ways to do it with 3 flips or more, but none with fewer than 3 flips.

In Case #2, all of the pancakes are already happy side up, so there is no need to flip any of them.

In Case #3, there is no way to make the second and third pancakes from the left have the same side up, because any flip flips them both. Therefore, there is no way to make all of the pancakes happy side up.

# Analysis


Oversized Pancake Flipper: Analysis
Let's start with two simple but key observations. First, the flips are commutative. That is, the order in which you make the flips doesn't matter: flipping at the same positions in any order always yields the same result. Second, you never need to flip at the same position more than once: since flips are commutative, you may rearrange the flips so that two flips at the same position happen consecutively, and then it is clear that they cancel each other out and you might as well not do either.

Small dataset
Applying the observations above to the Small dataset leaves only a really small number of combinations to try. Since there are N-K+1 possible flips, the number of flip subsets is 2N-K+1, which is at most 29 = 512 for this dataset. We can just try all of these combinations, discard the ones that leave at least one pancake blank side up, and get the minimum number of flips or determine that it is impossible.

Even if you don't have the observations above, a breadth-first search of all possible pancake states, using all possible flips as transitions, is also easily fast enough.

Large dataset
Of course, the approach above will take way too long for the Large dataset, which can have up to 1000 pancakes. There is a simple greedy strategy that is not too hard to find. Notice that the left-most pancake p1 is only affected by the left-most flip f1. That means that the initial status of p1 completely determines what do we need to do with f1 if we want to have any chance of leaving all pancakes happy side up: use f1 if and only if p1 is initially blank side up. After deciding on f1, we can notice that there is only one remaining flip f2 that affects the second to the left pancake p2. So, after we have used f1 (or not), the current state of p2 completely determines whether to use f2.

Continuing with this reasoning, we can use the leftmost N-K+1 pancakes to determine all flips. After doing that, we only need to check whether the last K-1 pancakes are happy side up or not. If they all are, then the answer is the number of flips we used. Otherwise, the answer is IMPOSSIBLE. Notice that this reasoning also implies that at most one of the subsets of flips from our Small-only solution above would have worked.

If we carry out the above strategy literally and actually flip all of the pancakes in memory each time, the complexity is O(N2). We can reduce this to O(N) by only flipping one pancake at a time, and keeping a running count of the number of flips that we "owe" the current pancake. For instance, suppose that N = 10 and K = 5, and the first pancake is blank side up. We start with the first pancake, and because we must flip it, we know we must flip the first five pancakes. We increase our flip count to 1, and also make a memo to decrease the flip count by 1 once we reach the sixth pancake. We continue from left to right, and whenever a pancake is blank side up and the flip count is even, or a pancake is happy side up and the flip count is odd, we increase the flip count and make another memo. These memos can be easily stored in another array of length N that is checked before handling each pancake. This optimization is not necessary to solve the Large dataset, but it is a useful trick in programming contest problems (and at least one of your Code Jam engineers has used it in day-to-day software engineering work!)
