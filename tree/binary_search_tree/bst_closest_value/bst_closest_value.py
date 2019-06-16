def closest_value(root, target):
    """
    :type root: TreeNode
    :type target: float
    :rtype: int
    """
    a = root.val
    kid = root.left if target < a else root.right
    if not kid:
        return a
    b = closest_value(kid, target)
    return min((a, b), key=lambda x: abs(target - x))
