class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        countS = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1 
        needs = len(countT) 
        has = 0 
        l = 0
        minLen = float("inf")
        ans = [-1, -1]
        for r in range(len(s)):
            char = s[r]
            countS[char] = countS.get(char, 0) + 1
            if countS[char] == countT.get(char, 0):
                has += 1 
            while has == needs:
                if r-l + 1 < minLen:
                    minLen = r-l + 1
                    ans = [l, r]
                char2 = s[l]
                if countS[char2] == countT.get(char2, 0):
                    has -= 1
                countS[char2] -= 1 
                l += 1 
        l,r = ans 
        return s[l:r+1] if minLen != float("inf") else ""
 

