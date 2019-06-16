# TC: O(b) SC: O(log n)
def is_symmetric(root):
    return _is_symmetric(root.left, root.right)


# notice this is very similar to is_same_tree but comparing left with right branches
def _is_symmetric(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None or q.val != p.val:
        return False
    return _is_symmetric(p.left, q.right) and _is_symmetric(p.right, q.left)


# same as above but using a stack
def is_symmetric_iterative(root):
    stack = [[root.left, root.right]]
    while stack:
        left, right = stack.pop()
        if left is None and right is None:
            continue
        if left is None or right is None:
            return False
        if left.val == right.val:
            stack.append([left.left, right.right])
            stack.append([left.right, right.right])
        else:
            return False
    return True
