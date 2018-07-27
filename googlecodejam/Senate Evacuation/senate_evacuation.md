Problem
A small fire started in the senate room, and it needs to be evacuated!

There are some senators in the senate room, each of whom belongs to of one of N political parties. Those parties are named after the first N (uppercase) letters of the English alphabet.

The emergency door is wide enough for up to two senators, so in each step of the evacuation, you may choose to remove either one or two senators from the room.

The senate rules indicate the senators in the room may vote on any bill at any time, even in the middle of an evacuation! So, the senators must be evacuated in a way that ensures that no party ever has an absolute majority. That is, it can never be the case after any evacuation step that more than half of the senators in the senate room belong to the same party.

Can you construct an evacuation plan? The senate is counting on you!

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of two lines. The first line contains a single integer N, the number of parties. The second line contains N integers, P1, P2, ..., PN, where Pi represents the number of senators of the party named after the i-th letter of the alphabet.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the evacuation plan. The plan must be a space-separated list of instructions, in the order in which they are to be carried out, where each instruction is either one or two characters, representing the parties of the senators to evacuate in each step.

It is guaranteed that at least one valid evacuation plan will exist. If multiple evacuation plans are valid, you may output any of them.

Limits
1 ≤ T ≤ 50.
No party will have an absolute majority before the start of the evacuation.
1 ≤ Pi ≤ 1000, for all i.
Time limit: 30 seconds per test set.
Memory limit: 1GB.

Test set 1 (Visible)
2 ≤ N ≤ 3.
sum of all Pi ≤ 9.

Test set 2 (Hidden)
2 ≤ N ≤ 26.
sum of all Pi ≤ 1000.

Sample

Input 
 	
Output 
 
4
2
2 2
3
3 2 2
3
1 1 2
3
2 3 1

Case #1: AB BA
Case #2: AA BC C BA
Case #3: C C AB
Case #4: BA BB CA

The sample output displays one set of answers to the sample cases. Other answers may be possible.

In Case #1, there are two senators from each of the parties A and B. If we remove one from each party every time, the perfect balance is maintained until evacuation is complete.

Case #2 proceeds as follows:

Initially in the room: 3 A, 2 B, 2 C.
Evacuate AA. Still in the room: 1 A, 2 B, 2 C.
Evacuate BC. Still in the room: 1 A, 1 B, 1 C.
Evacuate C. Still in the room: 1 A, 1 B.
Evacuate AB. Evacuation complete!

Note that it would not be valid to begin the evacuation with BC, which would leave 3 A, 1 B, and 1 C in the room; party A would have an absolute majority (3 out of 5 = 60%).

For Case #3, note that CC AB would also be a valid answer, and C C AB is also valid even though it requires three evacuation steps instead of two.




# Analisis

Senate Evacuation: Analysis
Small dataset
With at most three parties and at most nine senators, various brute force approaches will work. One exhaustive strategy is to generate all possible different evacuation orders, treating senators from the same party as interchangeable, and then try all possible different ways of chopping those into groups of one or two senators.

Another, simpler strategy is to keep randomly choosing and trying one of the nine possible evacuations (A, B, C, AA, AB, AC, BB, BC, CC) as long as the chosen senator(s) exist and the evacuation will not cause a new absolute majority. You may worry that this strategy could get stuck, but the outcome of any legal evacuation will just be another possible test case for the problem, and the statement guarantees that every test case has a solution! With more parties and senators, though, this strategy might bog down in the details of checking the legality of evacuations, so we should come up with a more efficient approach.

Large dataset
Intuitively, it is safest to remove one senator at a time, and to always draw from whichever party has the most remaining senators (or any such largest party, if there is a tie). But this strategy won't always work! For example, if we have two senators from party A and two from party B, and no others, which is a valid test case, then removing one senator from either party will give the other party an absolute majority.

However, this strategy is always safe whenever there are more than two parties present. Suppose that party 1 is currently the largest, or tied for the largest, of at least three parties, and that we remove a single senator from party 1. Clearly, making party 1 smaller cannot give it an absolute majority that it didn't have before. But could some other party acquire an absolute majority as a result? Suppose that the removal of a senator from party 1 were to cause party 2, which currently has X senators, to have an absolute majority. But since party 1 was the largest, or tied for the largest, before a senator was removed, party 1 must still have at least X-1 senators. Moreover, since at least one more party is present, there is at least 1 other senator who is not from party 1 or 2. So there are a total of at least X remaining senators who are not from party 2, which means the X senators of party 2 are not enough to give it an absolute majority, so we have a contradiction.

If we start with three or more parties and keep evacuating a single senator from the largest party in this way, then at some point, we must reach a step in which we go from three parties to two parties. These two remaining parties must have only one senator each. Since we just removed the one remaining senator from the third party, it must have been a largest party, so the other two can be no larger. So we can remove this last pair of senators in a single evacuation as a final step.

What if we start with two parties? Since the problem statement guarantees that no party begins with a majority, these parties must have equal numbers of senators. So, we can evacuate them in pairs, one from each party, until the evacuation is complete.

This approach takes more steps than are needed — most of those single evacuations can be paired up — but it gets the job done.
