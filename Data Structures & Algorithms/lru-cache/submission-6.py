class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity 
        self.left, self.right = Node(), Node()
        self.left.next, self.right.pre = self.right, self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        node = self.cache[key]
        self.move(node)
        self.add(node) 
        return node.val 

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return 
        if key in self.cache:
            old = self.cache[key]
            self.move(old) 
        new = Node(key, value)
        self.cache[key] = new 
        self.add(new)
        if len(self.cache) > self.cap:
            head = self.left.next 
            self.move(head)
            del self.cache[head.key]
    
    def move(self, node):
        pre, nxt = node.pre, node.next
        pre.next, nxt.pre = nxt, pre 

    def add(self, node):
        prev = self.right.pre 
        prev.next, node.pre = node, prev 
        self.right.pre, node.next = node, self.right 
    
class Node:
    def __init__(self, key=None, val = None):
        self.key = key 
        self.val = val 
        self.next = None 
        self.pre = None 