class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = [i for i in range(n)]
        for a, b in edges:
            rootA = self.find(p, a)
            rootB = self.find(p, b) 
            if rootA != rootB:
                p[rootA] = rootB
        ans = 0 
        for i in range(n): 
            if p[i] == i:
                ans += 1 
        return ans 
    def find(self, parent, node):
        stack = [] 
        while node != parent[node]:
            stack.append(node) 
            node = parent[node] 
        root = node 
        for node in stack:
            parent[node] = root 
        return root
