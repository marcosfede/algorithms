class SinglyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def is_cyclic(head):
    if not head:
        return False
    runner = head
    walker = head
    while runner.next and runner.next.next:
        runner = runner.next.next
        walker = walker.next
        if runner == walker:
            return True
    return False


def build_testcase(loop=False):
    head = SinglyLinkedListNode(0)
    prev = head
    for n in range(1, 100):
        new = SinglyLinkedListNode(n)
        prev.next = new
        prev = new
    loopstart = prev
    for n in range(100, 201):
        new = SinglyLinkedListNode(n)
        prev.next = new
        prev = new

    if loop:
        prev.next = loopstart

    return head


if __name__ == "__main__":
    loop = build_testcase(loop=True)
    noloop = build_testcase(loop=False)

    assert is_cyclic(loop) is True
    assert is_cyclic(noloop) is False
