class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        for a, b in edges:
            pa = self.find(parent, a)
            pb = self.find(parent, b)
            if pa == pb:
                return [a, b] 
            parent[pb] = pa
        return []
            
    def find(self, parent, node):
        curr = node 
        if curr != parent[curr]:
            parent[curr] = self.find(parent, parent[curr])
        return parent[node] 
        
        
    
