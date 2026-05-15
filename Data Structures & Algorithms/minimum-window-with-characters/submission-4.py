class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        countS = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1 
        needs = len(countT)
        has = 0 
        l = 0 
        ans = [-1, -1]
        minL = float("inf")
        for r in range(len(s)):
            c = s[r]
            countS[c] = countS.get(c, 0) + 1  
            if countS[c] == countT.get(c, 0):
                has += 1 
            while needs == has:
                if r - l + 1 < minL:
                    minL = r - l + 1 
                    ans = [l, r] 
                if countS[s[l]] == countT.get(s[l], 0):
                    has -= 1
                countS[s[l]] -= 1 
                l += 1 
        l, r = ans 
        return s[l:r+1] if minL != float("inf") else ""
