class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False 
        adj = [[] for _ in range(n)] 
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u) 

        visited = set() 
        q = collections.deque([0])
        visited.add(0) 
        while q:
            node = q.popleft() 
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei) 
                    q.append(nei) 
                    
        return len(visited) == n
                
