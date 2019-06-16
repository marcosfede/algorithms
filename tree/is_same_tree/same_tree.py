# Time Complexity O(min(N,M))
# where N and M are the number of nodes for the trees.

# Space Complexity O(min(height1, height2))
# levels of recursion is the mininum height between the two trees.


def is_same_tree(p, q):
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    return False
