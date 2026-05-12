class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        # 先对 tickets 排序，再反向遍历
        # 目的：让 adj[src] 中的目的地按【字典序从小到大】被 pop 出来
        # 因为 pop() 是从列表末尾取
        # [a, b], [a, c] [c, b] 
        # [c, b] [a, c] [a, b]
        for s, d in sorted(tickets)[::-1]:
            adj[s].append(d)
        stack = ["JFK"]
        res = []
        while stack:
            curr = stack[-1]
            if not adj[curr]:
                res.append(stack.pop())
            else:
                nxt = adj[curr].pop()
                stack.append(nxt)
        return res[::-1]