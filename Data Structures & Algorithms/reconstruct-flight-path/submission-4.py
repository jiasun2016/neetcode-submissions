class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for s, d in sorted(tickets)[::-1]:
            adj[s].append(d)
        stack = ["JFK"] 
        res = []
        while stack:
            curr = stack[-1]
            if adj[curr]:
                nxt = adj[curr].pop()
                stack.append(nxt) 
            else:
                res.append(curr) 
                stack.pop() 
        return res[::-1]
