class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjs = [[] for i in range(n)]
        for u, v in edges:
            adjs[u].append(v)
            adjs[v].append(u)
        visited = set()
        
        cnt = 0
        for i in range(n):
            if i not in visited:
                cnt += 1 
                visited.add(i)
                self.bfs(i, visited, adjs)
        return cnt

    def bfs(self, i, visited, adjs):
        q = collections.deque([i]) 
        while q:
            curr = q.popleft()
            for adj in adjs[curr]:
                if adj not in visited:
                    visited.add(adj)
                    q.append(adj) 
        
