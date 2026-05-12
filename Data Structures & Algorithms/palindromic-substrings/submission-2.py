class Solution:
    def countSubstrings(self, s: str) -> str:
        if not s:
            return 0
        ans = 0
        for mid in range(len(s)):
            ans += self.isPalindrome(s,mid,mid);
            ans += self.isPalindrome(s,mid,mid+1);
            
        return ans
           
    def isPalindrome(self, s, l, r):
        ans = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ans+= 1
            l -= 1 
            r += 1 
        return ans