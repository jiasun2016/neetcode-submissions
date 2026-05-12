class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.prev = self.next = None 

class LRUCache:
    def __init__(self, capacity: int): 
        self.cap = capacity 
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right  
        self.right.prev = self.left
        self.cache = {}

    def add(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node 
        node.next, node.prev = self.right, prev 
    
    def remove(self, node):
        prev, next = node.prev, node.next 
        prev.next, next.prev = next, prev 
        node.next = node.prev = None

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val 
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value  
            self.add(node)
        else:
            node = Node(key, value) 
            self.cache[key] = node
            self.add(node)
        if len(self.cache) > self.cap:
            lcr = self.left.next
            self.remove(lcr) 
            del self.cache[lcr.key]
        
