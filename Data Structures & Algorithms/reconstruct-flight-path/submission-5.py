class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for s,d in sorted(tickets)[::-1]:
            adj[s].append(d)
        q = ["JFK"] 
        res = []
        while q:
            curr = q[-1]
            if adj[curr]:
                nxt = adj[curr].pop()
                q.append(nxt) 
            else:
                res.append(q.pop()) 
        return res[::-1]