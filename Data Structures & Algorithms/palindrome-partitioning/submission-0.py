class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(0, s, [], res)
        return res

    def dfs(self, index, s, sub, res):
        if index == len(s):
            res.append(sub.copy()) 
            return 
        for i in range(index, len(s)):
            if not self.isPali(s, index, i):
                continue
            sub.append(s[index:i+1]) 
            self.dfs(i+1, s, sub, res)
            sub.pop()
        
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False 
            l += 1
            r -= 1  

        return True 