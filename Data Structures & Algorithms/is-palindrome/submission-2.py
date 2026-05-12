class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.isAlnum(s[l]):
                l +=1 
            while l < r and not self.isAlnum(s[r]):
                r -=1  
            if l < r and s[l].lower() != s[r].lower():
                return False
            l += 1 
            r -= 1  
        return True

    def isAlnum(self, s:str) -> bool:
        return (ord("a") <= ord(s) <= ord("z") or 
                ord("A") <= ord(s) <= ord("Z") or 
                ord("0") <= ord(s) <= ord("9"))

        