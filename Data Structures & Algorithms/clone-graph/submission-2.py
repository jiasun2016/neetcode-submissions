"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        newG = {}
        root = node
        if not node:
            return None
        newG[node] = Node(node.val) 
        que = deque([node])
        while que:
            node = que.popleft() 
            for nei in node.neighbors:
                if nei not in newG:
                    newG[nei] = Node(nei.val)   
                    que.append(nei)
                newG[node].neighbors.append(newG[nei]) 
        return newG[root]
