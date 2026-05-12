class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = [i for i in range(n)] 
        for a, b in edges:
            pa = self.find(p, a)
            pb = self.find(p, b) 
            if pa != pb:
                p[pa] = p[pb]
        ans = 0
        for i in range(n):
            if p[i] == i:
                ans += 1 
        return ans

    
    def find(self, parent, node):
        cur = node
        while cur != parent[cur]:
            parent[cur] =parent[parent[cur]]
            cur = parent[cur]
        return cur
