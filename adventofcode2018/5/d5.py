f = open('input')
chain = f.readline().strip()


class DLLNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev


class DLL:
    def __init__(self, chain):
        head = DLLNode(chain[0])
        prev = head
        for i in range(1, len(chain) - 1):
            curr = DLLNode(chain[i], prev)
            prev.next = curr
            prev = curr
        tail = DLLNode(chain[-1], prev)
        prev.next = tail
        self.head = head
        self.tail = tail

    def __len__(self):
        s = 1
        curr = self.head
        while curr.next is not None:
            s += 1
            curr = curr.next
        return s


class PolymerChain:
    def __init__(self, dll):
        self.dll = dll

    def react(self):
        curr = self.dll.head
        while curr.next is not None:
            next = curr.next
            if self.combusts(curr.val, next.val):
                prev = curr.prev
                if prev is None:
                    curr = next.next
                    curr.prev = None
                    self.dll.head = curr
                else:
                    prev.next, next.next.prev = next.next, prev
                    curr = prev
            else:
                curr = next

    def combusts(self, a, b):
        return b != a and a.lower() == b.lower()

    def __len__(self):
        return len(self.dll)

    def remove_unit(self, unit):
        curr = self.dll.head
        while curr.next is not None:
            next = curr.next
            if curr.val.lower() == unit:
                if curr.prev is None:
                    curr = next
                    curr.prev = None
                    self.dll.head = curr
                else:
                    prev = curr.prev
                    prev.next, next.prev = next, prev
                    curr = next
            else:
                curr = next


# p1
dll = DLL(chain)
p1 = PolymerChain(dll)
p1.react()
print(len(p1))

# p2
min_len = len(chain)
for letter in 'abcdefghijklmnopqrstuvwxyz':
    print(letter)
    dll = DLL(chain)
    p2 = PolymerChain(dll)
    p2.remove_unit(letter)
    p2.react()
    l = len(p2)
    if l < min_len:
        min_len = l
print(min_len)
