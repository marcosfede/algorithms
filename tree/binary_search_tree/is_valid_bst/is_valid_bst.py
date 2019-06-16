def is_BST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    stack = []
    pre = None
    while root and stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if pre and root.val <= pre.val:
            return False
        pre = root
        root = root.right
    return True
