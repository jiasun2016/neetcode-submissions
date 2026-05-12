class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for t in tasks:
            if t in d:
                d[t] += 1 
            else:
                d[t] = 1 
        counts = list(d.values())
        num_of_longest = 0 
        longest = max(counts) 
        for c in counts:
            if c == longest:
                num_of_longest+= 1
        # ans = (longest - 1) * (n + 1) + counts.count(longest)
        ans = (longest - 1)* (n+1) + num_of_longest
        return max(ans, len(tasks))
    