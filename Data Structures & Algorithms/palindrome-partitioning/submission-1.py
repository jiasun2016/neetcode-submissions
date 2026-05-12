class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, 0, [], res)
        return res 
    def dfs(self, s, index, sub, res):
        if index == len(s):
            res.append(list(sub))
            return
        for i in range(index, len(s)):
            if self.isPalindrome(s[index:i+1]):
                sub.append(s[index:i+1])
                self.dfs(s, i+1, sub, res)
                sub.pop()
    
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] != s[r]:
                return False 
            l += 1 
            r -= 1 
        return True 
    
    