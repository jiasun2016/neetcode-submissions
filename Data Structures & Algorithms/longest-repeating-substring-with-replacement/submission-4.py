class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        maxChar = 0
        count = {}
        maxL = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1 
            maxChar = max(maxChar, count[s[r]]) 
            while r-l + 1 - maxChar > k:
                count[s[l]] -= 1 
                l += 1  
            maxL = max(maxL, r-l + 1)
        return maxL
            

            