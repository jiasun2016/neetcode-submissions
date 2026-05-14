class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0 
        maxL = 0 
        maxFre = 0
        l = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1 
            maxFre = max(maxFre, count[s[r]]) 
            while r - l + 1- maxFre > k:
                count[s[l]] -= 1 
                l += 1
            maxL = max(maxL, r - l + 1)
        return maxL


