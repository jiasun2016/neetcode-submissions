class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for t in tasks:
            if t not in d:
                d[t] = 0 
            d[t] += 1 
        counts = list(d.values()) 
        longest = max(counts) 
        countlongest = 0 
        for c in counts:
            if c == longest:
                countlongest += 1 
        res = (longest - 1) * (n+1) + countlongest
        return max(res,len(tasks))
