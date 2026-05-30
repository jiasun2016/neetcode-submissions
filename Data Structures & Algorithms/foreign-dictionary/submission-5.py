class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for w in words:
            for c in w:
                if c not in adj:
                    adj[c] = set()
        indgree = {c:0 for c in adj} 
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2)) 
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                c1, c2 = w1[j], w2[j]
                if c1!= c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indgree[c2] += 1 
                    break 
        q = deque([])
        for c in indgree:
            if indgree[c] == 0:
                q.append(c)
        res = [] 
        while q:
            curr = q.popleft()    
            res.append(curr)
            for nxt in adj[curr]:
                indgree[nxt] -= 1
                if indgree[nxt] == 0:
                    q.append(nxt)
        return "".join(res) if len(res) == len(adj) else ""


