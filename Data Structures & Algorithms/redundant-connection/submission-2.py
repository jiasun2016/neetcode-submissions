class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p = [i for i in range(n+1)] 
        for n1, n2 in edges:
            p1 = self.find(p, n1)
            p2 = self.find(p, n2)
            if p1 == p2:
                return [n1, n2]
            else:
                p[p1] = p2 
        return [] 

    def find(self, parent, node):
        stack = []
        while node!= parent[node]:
            stack.append(node)
            node = parent[node]
        root = node 
        for node in stack:
            parent[node] = root 
        return root