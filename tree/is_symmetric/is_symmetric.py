# TC: O(b) SC: O(log n)
def is_symmetric(root):
    if not root:
        return True
    return helper(root.left, root.right)


def helper(p, q):
    if not p and not q:
        return True
    if not p or not q or q.val != p.val:
        return False
    return helper(p.left, q.right) and helper(p.right, q.left)


def is_symmetric_iterative(root):
    if not root:
        return True
    stack = [[root.left, root.right]]
    while stack:
        left, right = stack.pop()  # popleft
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val == right.val:
            stack.append([left.left, right.right])
            stack.append([left.right, right.right])
        else:
            return False
    return True
