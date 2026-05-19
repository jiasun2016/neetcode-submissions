class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res =[]
        self.dfs(s, [], res, 0)
        return res
    
    def dfs(self, s, sub, res, index):
        if index == len(s):
            res.append(list(sub))
            return 
        for i in range(index, len(s)):
            cut = s[index:i+1]
            
            if not self.isValid(cut):
                continue
            sub.append(cut)
            self.dfs(s, sub, res, i+1)
            sub.pop()

        
    def isValid(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False 
            l += 1 
            r -= 1 
        return True 