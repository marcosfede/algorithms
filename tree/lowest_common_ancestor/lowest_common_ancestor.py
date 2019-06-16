def LCA(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if not root or root is p or root is q:
        return root
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    if left and right:
        return root
    return left if left else right
