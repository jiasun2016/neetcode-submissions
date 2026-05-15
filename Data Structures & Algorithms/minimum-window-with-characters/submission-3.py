class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1 
        needs= len(countT) 
        has = 0 
        countS = {}
        l = 0 
        minLen = float("inf")
        ans = [-1, -1]
        for r in range(len(s)):
            countS[s[r]] = countS.get(s[r], 0)+1
            if countS[s[r]] == countT.get(s[r], 0):
                    has += 1 
            while needs == has:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    ans = [l,r] 
                if countS[s[l]] == countT.get(s[l], 0):
                    has -= 1
                countS[s[l]] -= 1 
                l += 1 
        l, r = ans    
        return s[l:r+1] if minLen != float("inf") else ""