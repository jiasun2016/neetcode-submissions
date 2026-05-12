class Node:
    def __init__(self, key, val):
        self.val = val 
        self.key = key 
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.keyToPre = {}  
        self.dummy = Node(-1,-1)
        self.tail = self.dummy 
        
    def get(self, key: int) -> int:
        if key not in self.keyToPre:
            return -1 
        pre = self.keyToPre[key] 
        val = pre.next.val 
        self.moveToEnd(pre)
        return val

    def moveToEnd(self,pre):
        if pre.next != self.tail:
            node = pre.next 
            pre.next = node.next 
            self.keyToPre[node.next.key] = pre 
            node.next = None
            self.addToEnd(node) 

    def addToEnd(self, node):
        self.tail.next = node 
        self.keyToPre[node.key] = self.tail  
        self.tail = node 
    
    def put(self, key: int, value: int) -> None:
        if key in self.keyToPre:
            node = self.keyToPre[key].next 
            node.val = value 
            self.moveToEnd(self.keyToPre[key]) 
        else:
            node = Node(key, value) 
            self.addToEnd(node) 
            if len(self.keyToPre) > self.cap:
                self.removeHead()
    def removeHead(self):
        head = self.dummy.next
        if head.next:
            self.dummy.next = head.next
            del self.keyToPre[head.key]
            self.keyToPre[head.next.key] = self.dummy 
            head.next = None 
