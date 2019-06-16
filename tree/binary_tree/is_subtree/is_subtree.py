from collections import deque


def is_subtree(big, small):
    flag = False
    queue = deque()
    queue.append(big)
    while queue:
        node = queue.popleft()
        if node.val == small.val:
            flag = comp(node, small)
            break
        else:
            queue.append(node.left)
            queue.append(node.right)
    return flag


def comp(p, q):
    if not p and not q:
        return True
    if p and q:
        return p.val == q.val and comp(p.left, q.left) and comp(p.right, q.right)
    return False
