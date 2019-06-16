def lowest_common_ancestor(root, p, q):
    """
    :type root: Node
    :type p: Node
    :type q: Node
    :rtype: Node
    """
    while root:
        if p.val > root.val < q.val:
            root = root.right
        elif p.val < root.val > q.val:
            root = root.left
        else:
            return root
