class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return "" 
        countT, window = {}, {} 
        for c in t:
            countT[c] = countT.get(c, 0) + 1 
        needs = len(countT)
        have = 0 
        ans = [-1, -1]
        l = 0
        ansLen = float('infinity')
        for r in range(len(s)):
            char = s[r] 
            window[char] = window.get(char, 0) + 1 
            if char in countT and window[char] == countT[char]:
                have += 1 
            while have == needs:
                if r-l+1 < ansLen:
                    ansLen = r-l+1 
                    ans = [l, r] 
                preChar = s[l]
                if preChar in countT and window[preChar] == countT[preChar]:
                    have -= 1
                window[preChar] -= 1
                l += 1   
        l, r = ans 
        return s[l:r+1] if ansLen != float('infinity') else ""

        


