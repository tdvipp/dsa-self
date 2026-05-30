class ListNode:
    def __init__(self, key: int | None = None, val: int | None = None): 
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.len = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {} # key -> Node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            prev = node.prev
            nex = node.next
            prev.next = nex
            nex.prev = prev

            # move it to tail
            self.tail.prev.next = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            prev = node.prev
            nex = node.next
            prev.next = nex
            nex.prev = prev

            node.val = value
        else:
            if self.len == self.cap:
                # remove least recently used key which is at head
                tmp = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.map[tmp.key]
                del tmp
                self.len -= 1

            node = ListNode(key, value)
            self.map[key] = node
            self.len += 1
        # move it to tail
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node