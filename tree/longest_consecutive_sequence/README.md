Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
```
   1
    \
    3
   / \
  2   4
       \
        5
```
Longest consecutive sequence path is 3-4-5, so return 3.

===============
```
       10
      /    \     
     /      \
    11        9    
   / \        /\
  /   \      /  \
13    12    13   8
```
Maximum Consecutive Path Length is 3 (10, 11, 12)
Note: 10, 9 ,8 is NOT considered since

===============
```
           5
          /  \
         /    \
        8      11
        /        \
       /          \
       9          10   
      /           /
     /           /
    6           15
```
Maximum Consecutive Path Length is 2 (8, 9).
