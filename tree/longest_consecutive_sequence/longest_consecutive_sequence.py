maxlen = 0


def longestConsecutive(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    DFS(root, 0, root.val)
    return maxlen


def DFS(root, cur, target):
    global maxlen
    if not root:
        return
    if root.val == target:
        cur += 1
    else:
        cur = 1
    maxlen = max(cur, maxlen)
    DFS(root.left, cur, root.val + 1)
    DFS(root.right, cur, root.val + 1)
