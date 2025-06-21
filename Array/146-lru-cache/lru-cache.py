class ListNode:
    def __init__(self, key=-1, val=-1):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
       self.capacity = capacity
       self.left = ListNode()
       self.right = ListNode()
       self.left.next = self.right
       self.right.prev = self.left
       self.map = {}

    def remove(self, node: ListNode) -> ListNode:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        return node
    
    def insertAtRight(self, node:ListNode) -> None:
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        
        self.right.prev = node
        node.next = self.right

    def get(self, key: int) -> int:
        
        if key in self.map:
            node = self.remove(self.map[key])
            self.insertAtRight(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        node = ListNode(key, value)

        if key in self.map:
            self.remove(self.map[key])
        else:
            if  1+len(self.map) > self.capacity:
                leftNode = self.remove(self.left.next)
                del self.map[leftNode.key]
        self.map[key] = node
        self.insertAtRight(node)

        




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)