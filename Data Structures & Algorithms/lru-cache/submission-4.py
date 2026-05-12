class Node:
    def __init__(self, key, val):
        self.val = val 
        self.key = key 
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.key2pre = {}
        self.tail = Node(-1,-1)
        self.dummy = self.tail
        
    def get(self, key: int) -> int:
        if key not in self.key2pre:
            return -1 
        pre = self.key2pre[key]
        val = pre.next.val
        self.move2end(pre)
        return val
    
    def move2end(self, pre):
        if pre.next != self.tail:
            node = pre.next
            pre.next = node.next 
            self.key2pre[node.key] = None 
            self.key2pre[node.next.key] = pre
            node.next = None 
            self.add2end(node)
    def add2end(self, node):
        self.tail.next = node 
        self.key2pre[node.key] = self.tail 
        self.tail = node


    def put(self, key: int, value: int) -> None:
        if key in self.key2pre:
            pre = self.key2pre[key]
            node = pre.next 
            node.val = value 
            self.move2end(pre) 
        else:
            node = Node(key, value)
            self.add2end(node) 
            if len(self.key2pre) > self.cap:
                self.removeHead()
    def removeHead(self):
        head = self.dummy.next 
        if head.next:
            self.dummy.next = head.next 
            del self.key2pre[head.key]
            self.key2pre[head.next.key] = self.dummy 
            head.next = None 

        
