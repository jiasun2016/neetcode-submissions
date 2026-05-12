class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        ans = ""
        for mid in range(len(s)):
            substring = self.isPalindrome(s,mid,mid);
            if len(substring) > len(ans):
                ans = substring
            substring2 = self.isPalindrome(s,mid,mid+1);
            if len(substring2) > len(ans):
                ans = substring2
        return ans
           
    def isPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1 
            r += 1 
        return s[l+1:r] 