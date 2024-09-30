class Node:
    def __init__(self, freq):
        self.freq = freq
        self.next = None
        self.prev = None
        self.keys = set()


# Doubly LinkedList
class AllOne:

    def __init__(self):
        self.head = Node(0)  # dummy head node
        self.tail = Node(0)  # dummy tail node
        self.head.next = self.tail
        self.head.prev = self.head
        self.map = {}  # stores nodes

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            freq = node.freq
            node.keys.remove(key)
            nextNode = node.next

            # Condition to create a new node
            if nextNode == self.tail or freq + 1 != nextNode.freq:
                newNode = Node(freq + 1)
                newNode.keys.add(key)
                newNode.prev = node
                newNode.next = nextNode
                node.next = newNode
                nextNode.prev = newNode
                self.map[key] = newNode
            else:
                nextNode.keys.add(key)
                self.map[key] = nextNode
            if not node.keys:
                self.removeNode(node)
        else:  # Key does not exist
            firstNode = self.head.next
            # Condition to create a new node
            if firstNode == self.tail or firstNode.freq > 1:
                newNode = Node(1)
                newNode.keys.add(key)
                newNode.next = firstNode
                newNode.prev = self.head
                firstNode.prev = newNode
                self.head.next = newNode
                self.map[key] = newNode
            else:
                firstNode.keys.add(key)
                self.map[key] = firstNode

    def dec(self, key: str) -> None:
        node = self.map[key]
        node.keys.remove(key)
        freq = node.freq

        if freq == 1:
            del self.map[key]
        else:
            prevNode = node.prev
            # Condition to create a new node
            if prevNode == self.head or prevNode.freq != freq - 1:
                newNode = Node(freq - 1)
                newNode.keys.add(key)
                newNode.prev = prevNode
                newNode.next = node
                node.prev = newNode
                prevNode.next = newNode
                self.map[key] = newNode
            else:
                prevNode.keys.add(key)
                self.map[key] = prevNode
        if not node.keys:
            self.removeNode(node)

    def getMaxKey(self) -> str:
        if self.head.next == self.tail: return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail: return ""
        return next(iter(self.head.next.keys))

    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
