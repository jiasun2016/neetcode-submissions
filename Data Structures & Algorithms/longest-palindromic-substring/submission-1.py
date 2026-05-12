class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        ans = ""
        for mid in range(len(s)):
            subStrings = self.isPalindrome(s, mid, mid)
            if len(subStrings) > len(ans):
                ans = subStrings
            subStrings2 = self.isPalindrome(s, mid, mid+1)
            if len(subStrings2) > len(ans):
                ans = subStrings2
        return ans 
        
    def isPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l]== s[r]:
            l -= 1 
            r += 1
        return s[l+1:r]