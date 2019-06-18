## Balanced trees
the tree is only balanced if:

The left and right subtrees' heights differ by at most one, AND
The left subtree is balanced, AND
The right subtree is balanced

this ensures O(log(n)) searches

According to this, the next tree is balanced:
```
     A
   /   \
  B     C  
 /     / \  
D     E   F  
     /  
    G  
```
The next one is not balanced because the subtrees of C differ by 2 in their height:
```
     A
   /   \
  B     C   <-- difference = 2
 /     /
D     E  
     /  
    G  
```

There are many ways to keep a tree balanced, see types of trees for details


## Complete trees
A complete binary tree is a binary tree in which every level of the tree is fully filled, except for perhaps the
last level. To the extent that the last level is filled, it is filled left to right.
A complete tree is always balanced. Reciprocal is not true

## Full Binary Trees
A full binary tree is a binary tree in which every node has either zero or two children. That is, no nodes have
only one child.

## Perfect Binary Trees
A perfect binary tree is one that is both full and complete. All leaf nodes will be at the same level, and this
level has the maximum number of nodes.

## Tree Traversal

- In-Order Traversal:
  - visit left children
  - visit node
  - visit right children

- Pre-Order Traversal
  - visit node
  - visit left children
  - visit right children

- Post-Order Traversal
  - visit left children
  - visit right children
  - visit node



# Type of trees

## Binary trees
Trees with at most 2 children per node

## Binary Search trees (BST)
A binary search tree is a binary tree in which every node fits a specific ordering property:
all left descendants <= n < all right descendents. This must be true for each node n
Note that this inequality must be true for all of a node's descendents, not just its immediate children
visualization: https://www.cs.usfca.edu/~galles/visualization/BST.html

## B Tree
Self-balancing search tree

Unlike other self-balancing binary search trees, the B-tree is well suited for storage systems that read and write relatively large blocks of data, such as discs. It is commonly used in databases and file systems.

B-trees have substantial advantages over alternative implementations when the time to access the data of a node greatly exceeds the time spent processing that data, because then the cost of accessing the node may be amortized over multiple operations within the node. This usually occurs when the node data are in secondary storage such as disk drives. By maximizing the number of keys within each internal node, the height of the tree decreases and the number of expensive node accesses is reduced. In addition, rebalancing of the tree occurs less often

MIT Lesson: https://www.youtube.com/watch?v=TOb1tuEZ2X4
visualization: https://www.cs.usfca.edu/~galles/visualization/BTree.html

## B+ Tree
A B+ tree can be viewed as a B-tree in which each node contains only keys (not key–value pairs), and to which an additional level is added at the bottom with linked leaves.

- The leaf nodes of B+ trees are linked, so doing a full scan of all objects in a tree requires just one linear pass through all the leaf nodes. A B tree, on the other hand, would require a traversal of every level in the tree. This full-tree traversal will likely involve more cache misses than the linear traversal of B+ leaves.
- Because B+ trees don't have data associated with interior nodes, more keys can fit on a page of memory. Therefore, it will require fewer cache misses in order to access data that is on a leaf node.

visualization: https://www.cs.usfca.edu/~galles/visualization/BPlusTree.html

## B vs B+ bs B*

| B                                                               | B+                                                   | B*                      |
| --------                                                        | --------                                             | --------                |
| Keys & data can be stored in both the internal & leaf nodes     | Keys & data can only be stored in the leaf nodes     | same as b+              |
| No redundancy of keys                                           | some duplication of keys                             | same as b+              |
| nodes not linked with each other (sequential scan costly)       | leaf nodes are linked together, fast seq access      | same as b+              |
| deletion of data is costly bc we've to find data at diff levels | deletion is easier as all data found at leaf nodes   | more complicated than b+|
| nodes at least 1/2 full                                         | nodes at least 1/2 full                              | nodes at least 2/3 full |

- all are balanced
- all have leafs at same level
- key values are arranged in increasing order
- all hold BST properties
- used to store data on external storage

## AVL Tree
Self-balancing binary search tree

In an AVL tree, the heights of the two child subtrees of any node differ by at most one, rebalancing is done to restore this property

Insertions and deletions may require the tree to be rebalanced by one or more tree rotations.

visualization: https://www.cs.usfca.edu/~galles/visualization/AVLtree.html

## Red Black Tree
Self-balancing binary search tree
Each node of the binary tree has an extra bit, and that bit is often interpreted as the color (red or black) of the node. 
These color bits are used to ensure the tree remains approximately balanced during insertions and deletions

In addition to the requirements imposed on a binary search tree the following must be satisfied by a red–black tree:
- Each node is either red or black.
- The root is black. This rule is sometimes omitted. Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.
- All leaves (NIL) are black.
- If a node is red, then both its children are black.
- Every path from a given node to any of its descendant NIL nodes contains the same number of black nodes.

visualization: https://www.cs.usfca.edu/~galles/visualization/RedBlack.html

## Tries, aka prefix-tree

A trie is a variant of an n-ary tree in which characters are stored at each node. Each path down the tree may
represent a word.

Very commonly, a trie is used to store the entire (English) language for quick prefix lookups. While a hash
table can quickly look up whether a string is a valid word, it cannot tell us if a string is a prefix of any valid
words. A trie can do this very quickly.

visualization: https://www.cs.usfca.edu/~galles/visualization/Trie.html