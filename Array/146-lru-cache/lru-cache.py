class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def remove(self, node: Node) -> Node:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insertAtTail(self, node):
        node.next = self.tail
        prev = self.tail.prev 
        prev.next = node
        self.tail.prev = node
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.insertAtTail(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        newNode = Node(key, value)
        if key in self.map:
            self.remove(self.map[key])
        else:
            if len(self.map.keys())+1 > self.capacity:
                node = self.head.next
                self.remove(node)
                del self.map[node.key]
        self.insertAtTail(newNode)
        self.map[key] = newNode


        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)