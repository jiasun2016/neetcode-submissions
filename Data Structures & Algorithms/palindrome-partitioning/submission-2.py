class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.dfs(s, [], 0, ans)
        return ans 

    def dfs(self, s, sub, i, ans):
        if i == len(s):
            ans.append(list(sub))
            return
        
        for j in range(i, len(s)):
            if self.isPalindrome(s[i:j+1]):
                sub.append(s[i:j+1])
                self.dfs(s, sub, j+1, ans)
                sub.pop()

        
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1 
            while l < r and not s[r].isalnum():
                r -= 1 
            if s[l].lower() != s[r].lower():
                return False 
            l += 1
            r -= 1
        return True 