class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        maxFreq = 0 
        l = 0 
        res = 0 
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1 
            maxFreq = max(seen[s[r]], maxFreq) 
            while (r-l+ 1) - maxFreq  > k:
                seen[s[l]] -= 1
                l += 1 
            res = max(res, r-l+ 1) 
        return res 
