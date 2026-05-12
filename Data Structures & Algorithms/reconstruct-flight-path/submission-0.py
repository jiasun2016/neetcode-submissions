class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list) 
        tickets.sort()
        print(tickets) 
        for a, b in tickets:
            adj[a].append(b) 
        stack = []
        self.dfs("JFK", adj, stack)
        print(stack) 
        return stack[::-1]

    def dfs(self, node, adj, stack):
        while adj[node]:
            nei = adj[node].pop(0) 
            self.dfs(nei, adj, stack) 
        stack.append(node)


