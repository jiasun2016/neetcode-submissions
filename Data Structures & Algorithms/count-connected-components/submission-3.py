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
    def find(self, p, node):
        root = node 
        # find root 
        while p[root]!= root:
            root = p[root]
        curr = node
        while curr != root:
            temp = p[curr]
            p[curr] = root 
            curr = temp 
        return root 

