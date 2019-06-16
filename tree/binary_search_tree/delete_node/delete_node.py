def delete_node(root, key):
    """
    :type root: TreeNode
    :type key: int
    :rtype: TreeNode
    """
    if not root:
        return None

    if root.val == key:
        if root.left:
            # Find the right most leaf of the left sub-tree
            left_right_most = root.left
            while left_right_most.right:
                left_right_most = left_right_most.right
            # Attach right child to the right of that leaf
            left_right_most.right = root.right
            # Return left child instead of root, a.k.a delete root
            return root.left
        else:
            return root.right
    # If left or right child got deleted, the returned root is the child of the deleted node.
    elif root.val > key:
        root.left = delete_node(root.left, key)
    else:
        root.right = delete_node(root.right, key)
    return root
