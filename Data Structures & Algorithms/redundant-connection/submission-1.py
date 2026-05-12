class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) 
        parent = [i for i in range(n+1)] 

        for n1, n2 in edges:
            p1 = self.find(parent, n1) 
            p2 = self.find(parent, n2) 
            if parent[p1] ==  parent[p2]:
                return [n1, n2]  
            else:
                parent[p1] =  parent[p2] 
        return []

    # def find(self, parent, node):
    #     curr = node
    #     while curr != parent[curr]:
    #         parent[curr] = parent[parent[curr]]
    #         curr = parent[curr] 
    #     return curr
    
    def find(self, parent, node):
        stack = []
        curr = node
        while curr != parent[curr]:
            stack.append(curr)
            curr = parent[curr] 
        root = curr 
        for node in stack:
            parent[node] = root 
        return root
