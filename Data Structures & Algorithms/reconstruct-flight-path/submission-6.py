class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjs = collections.defaultdict(list)
        for s, d in sorted(tickets)[::-1]:
            adjs[s].append(d) 
        q = ["JFK"]
        res = []
        while q:
            curr = q[-1]
            if adjs[curr]:
                nxt = adjs[curr].pop()
                q.append(nxt) 
            else:
                res.append(q.pop())

        return res[::-1]
