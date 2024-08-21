# Lowest Common Ancestor in Binary Tree

## Problem Statement

Given a binary tree and two nodes in the tree, find the lowest common ancestor (LCA) of the two nodes. The lowest common ancestor is defined as the deepest node in the tree that is an ancestor of both nodes.

For this problem, we allow a node to be a descendant of itself. In other words, if either of the input nodes is the root of the tree, the root should be returned as the LCA.

## Input Format

- A binary tree represented by its root node.
- Two nodes, `p` and `q`, which are present in the binary tree.

## Expected Output

Return the node that is the lowest common ancestor of nodes `p` and `q`.

## Example

Consider the following binary tree:

```
       3
     /   \
    5     1
   / \   / \
  6   2 0   8
     / \
    7   4
```

- If `p = 5` and `q = 1`, the LCA is `3`.
- If `p = 5` and `q = 4`, the LCA is `5`.
- If `p = 6` and `q = 4`, the LCA is `5`.

## Constraints

- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- `p` and `q` are guaranteed to exist in the tree.
- `p != q`

## Follow-up

Can you implement a solution with O(n) time complexity, where n is the number of nodes in the tree?
