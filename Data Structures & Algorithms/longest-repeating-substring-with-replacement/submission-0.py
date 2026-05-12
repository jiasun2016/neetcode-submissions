class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        maxFre = 0 
        l = 0
        res = 0
        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1 
            maxFre = max(maxFre, counter[s[r]]) 
            while (r-l+1)- maxFre > k:
                counter[s[l]] -= 1 
                maxFre = max(maxFre, counter[s[l]]) 
                l += 1 
            res = max(res, r-l+1) 
        return res
            
