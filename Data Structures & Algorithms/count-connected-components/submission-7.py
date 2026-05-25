

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a,b) 
        return uf.count 

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n 
        self.size = [1] * n 

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]

    def union(self, a, b):        
        parentA, parentB = self.find(a), self.find(b)
        if parentA == parentB:
            return 
        if self.size[parentA] < self.size[parentB]:
            a, b = b, a 
        self.parent[parentB] =  parentA 
        self.size[parentA] += self.size[parentB]
        self.count -= 1
        return True 

