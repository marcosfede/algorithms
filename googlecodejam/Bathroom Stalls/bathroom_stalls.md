Problem
A certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends are permanently occupied by the bathroom guards. The other N stalls are for users.

Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible. To avoid confusion, they follow deterministic rules: For each empty stall S, they compute two values LS and RS, each of which is the number of empty stalls between S and the closest occupied stall to the left or right, respectively. Then they consider the set of stalls with the farthest closest neighbor, that is, those S for which min(LS, RS) is maximal. If there is only one such stall, they choose it; otherwise, they choose the one among those where max(LS, RS) is maximal. If there are still multiple tied stalls, they choose the leftmost stall among those.

K people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.

When the last person chooses their stall S, what will the values of max(LS, RS) and min(LS, RS) be?

Solving this problem
This problem has 2 Small datasets and 1 Large dataset. You must solve the first Small dataset before you can attempt the second Small dataset. You will be able to retry either of the Small datasets (with a time penalty). You will be able to make a single attempt at the Large, as usual, only after solving both Small datasets.

Input
The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with two integers N and K, as described above.

Output
For each test case, output one line containing Case #x: y z, where x is the test case number (starting from 1), y is max(LS, RS), and z is min(LS, RS) as calculated by the last person to enter the bathroom for their chosen stall S.

Limits
1 ≤ T ≤ 100.
1 ≤ K ≤ N.
Small dataset 1
1 ≤ N ≤ 1000.
Small dataset 2
1 ≤ N ≤ 106.
Large dataset
1 ≤ N ≤ 1018.
Sample

Input 
 	
Output 
 
5
4 2
5 2
6 2
1000 1000
1000 1

Case #1: 1 0
Case #2: 1 0
Case #3: 1 1
Case #4: 0 0
Case #5: 500 499

In Case #1, the first person occupies the leftmost of the middle two stalls, leaving the following configuration (O stands for an occupied stall and . for an empty one): O.O..O. Then, the second and last person occupies the stall immediately to the right, leaving 1 empty stall on one side and none on the other.

In Case #2, the first person occupies the middle stall, getting to O..O..O. Then, the second and last person occupies the leftmost stall.

In Case #3, the first person occupies the leftmost of the two middle stalls, leaving O..O...O. The second person then occupies the middle of the three consecutive empty stalls.

In Case #4, every stall is occupied at the end, no matter what the stall choices are.

In Case #5, the first and only person chooses the leftmost middle stall.




# Analysis

Bathroom Stalls: Analysis
Small dataset 1
For Small dataset 1, the limits are small enough that you can just simulate the rules outlined in the statement. Most implementations of a simulation will run in O(NK) time and thus finish immediately, but even a slow O(N2K) implementation like "try every possible stall for the next person, and for each empty stall run a loop for each side to check for the closest neighbors" will most likely finish in time.

For Small dataset 2 and the Large dataset, however, something quadratic in the number of stalls won't cut it, so we have to do better.

Small dataset 2
The critical observation to jump from Small dataset 1 to Small dataset 2 is that only the number of consecutive runs of empty stalls matters at any given time. The next person always chooses the middle stall or the left of the two middle stalls of a longest subsequence of consecutive empty stalls. Moreover, the output format already hints at this: even if you were to choose the rightmost of a set of two middle stalls, or a longest run of stalls other than the leftmost one, the answer would not change. Thus, we can rewrite the algorithm in this equivalent (for the required output) form:

Find any longest subsequence of consecutive empty stalls.
Choose the middle or one of the two middle stalls.
Notice that even though there are still ties to be broken, the output is equivalent for all of them. Since the output is equivalent, so is the multiset of lengths of consecutive runs of empty stalls left behind, so the whole process only depends on that multiset. (As a reminder, a multiset is a set in which the same element can appear more than once.) We can write an optimized simulation that solves Small dataset 2 following this pseudocode:

  S = {N}  - This is a multiset!
  repeat K times:
    X = max(S)
    X0 = ceil((X - 1) / 2)
    X1 = floor((X - 1) / 2)
    if this is the last step:
      we are done; answer is X0 and X1
    else:
      remove one instance of X from S
      insert X0 and X1 into S
If the operations over S are efficient, this will run in quasilinear time. There are many data structures that support insertion, finding the maximum, and removal of the maximum in logarithmic time, including AVL trees, red-black trees, and heaps. Many languages have one such structure in their standard libraries (e.g., the multiset or priority_queue in C++, TreeSet in Java, and heapq module in Python). Since we take O(log K) time for each of K steps, the algorithm takes only O(K log K) time, which is fast enough to solve Small dataset 2. However, for the Large dataset, even quasilinear time on K is not enough.

Large dataset
The observation required to solve the Large dataset is that we are simulating similar steps over and over again. The first time a bathroom user arrives, we partition N into ceil((N - 1) / 2) and floor((N - 1) / 2), which means that numbers between ceil((N - 1) / 2) and N will never appear in S. This hints at a logarithmic number of simulation steps.

Let's divide the work in stages. The first stage processes only N. Then, stage i+1 processes all of the values spawned by stage i. So, stage 2 processes up to 2 values: ceil((i - 1) / 2) and floor((i - 1) / 2). What about the other stages? It is not hard to prove by induction that they also process at most two consecutive values: since stage i processes two consecutive values, they are either 2x and 2x+1 or 2x and 2x-1, for some x (that is, one even and one odd number). Thus, the spawned values for stage i+1 can only be x and/or x-1. Since the largest value in each stage is at most half the largest value of the previous stage, there are a logarithmic number of stages. This all means that there are at most O(log N) different values that go into S at any point. Of course, some of them appear in S many, many times. So, the optimization to get the running time low enough for the Large dataset is to process all repetitions of a given value at the same time, since all of them yield the same X0 and X1 values. We can do that by using a regular set with a separate count for the number of repetitions.

  S = {N}  - This is a set, not a multiset!
  C(N) = 1
  P = 0
  repeat:
    X = max(S)
    X0 = ceil((X - 1) / 2)
    X1 = floor((X - 1) / 2)
    P = P + C(X)
    if P ≥ K:
      we are done; the answer is X0 and X1.
    else:
      remove X from S
      insert X0 and X1 into S
      add C(X) to the counts of X0 and X1 in C
Once again, we have structures that implement all the required operations in logarithmic time, yielding an O(log2 N) running time overall. In general, adding any good dictionary implementation to the structure of choice from the Small dataset 2 solution would work, either by plugging the dictionary functionality into the structure (like map in C++ or TreeMap in Java) or having a separate hash-table for the dictionary (which is the easiest implementation in Python).

Moreover, since we proved the population of S is at most 4 at any given time (only values from two consecutive stages can coexist in S), any implementation of set and dictionary will provide all operations in constant time, because the size of the whole structure is bounded by a constant! This makes the overall time complexity just O(log N).

This was a nice problem to put experimentation to work if your intuition was not enough. After solving the Small, if you print the succession of values for a fixed N, you may spot the pattern of few values occurring in the set S, and from there, you can find the mathematical arguments to support the needed generalization. In harder problems in later rounds, this can become an even more important asset to tackle problems. As you can see in many parts of last year's finals live stream, finalists use experimentation a lot to inspire themselves and/or validate their ideas before committing to them.
