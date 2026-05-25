class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False 
        adjs = [[] for i in range(n)]
        for u, v in edges:
            adjs[u].append(v)
            adjs[v].append(u)
        visited = set()
        q = collections.deque([0])
        visited.add(0)
        while q:
            curr = q.popleft()
            for adj in adjs[curr]:
                if adj not in visited:
                    visited.add(adj)
                    q.append(adj) 
        return len(visited) == n
