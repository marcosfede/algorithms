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

