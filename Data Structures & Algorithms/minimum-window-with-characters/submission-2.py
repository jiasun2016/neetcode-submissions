class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        minLen = float("infinity")
        res = [-1, -1]
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        has, need = 0,0
        need = len(countT)
        l = 0 
        for r in range(len(s)):
            c = s[r] 
            window[c] = window.get(c, 0) + 1 
            if window[c] == countT.get(c, 0):
                has += 1 
            while has == need:
                if(r-l +1) < minLen:
                    minLen = r-l +1 
                    res = [l, r] 
                if s[l] in countT and countT[s[l]] == window[s[l]]:
                    has -= 1
                window[s[l]] -= 1 
                l += 1 
        l, r = res 
        return s[l: r+1] if minLen != float("infinity") else ""

                

                



        
        