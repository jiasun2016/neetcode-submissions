class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = [i for i in range(n)]
        for a, b in edges:
            rootA = self.find(p, a)
            rootB = self.find(p, b)
            if rootA != rootB:
                p[rootA] = rootB
        cnt = 0
        for i in range(n):
            if p[i] == i:
                cnt += 1
        return cnt 
                

    def find(self, parent, node):
        curr = node 
        stack = []
        while curr != parent[curr]:
            stack.append(curr)
            curr = parent[curr]
        for node in stack:
            parent[node] = curr 
        return curr