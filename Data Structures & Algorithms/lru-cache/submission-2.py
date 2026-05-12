class Node:
    def __init__(self, value=None, key=None, next=None):
        self.key = key 
        self.value = value 
        self.next = next 
        
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity 
        self.dummy = Node() 
        self.tail = self.dummy 
        self.key_to_pre = {} 

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here 
        if key not in self.key_to_pre:
            return -1  
        pre = self.key_to_pre[key] 
        value = pre.next.value
        self.move_to_tail(pre) 
        return value 
        
    def move_to_tail(self, pre):
        if pre.next == self.tail:
            return 
        node = pre.next 
        pre.next = node.next
        self.key_to_pre[node.next.key] = pre 
        node.next = None
        self.add_to_tail(node) 
        
    def add_to_tail(self, node):
        self.tail.next = node 
        self.key_to_pre[node.key] = self.tail 
        self.tail = node 


    def put(self, key, value):
        if key in self.key_to_pre:
            pre = self.key_to_pre[key]
            pre.next.value = value 
            self.move_to_tail(pre) 
        else:
            node = Node(value, key)
            self.add_to_tail(node)
            if len(self.key_to_pre) > self.capacity:
                self.remove_first() 
                
    def remove_first(self):
        head = self.dummy.next 
        if head.next:
            self.dummy.next = head.next 
            del self.key_to_pre[head.key]
            self.key_to_pre[head.next.key] = self.dummy