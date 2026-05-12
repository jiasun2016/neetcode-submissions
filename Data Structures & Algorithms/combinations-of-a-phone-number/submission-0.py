dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        self.dfs(0, digits, "", res)
        return res 
        
    def dfs(self, index, digits, curStr, res):
        if len(curStr) == len(digits):
            res.append(curStr) 
            return 
        for i in range(index, len(digits)):
            n = digits[i]
            for c in dic[n]:
                
                self.dfs(i+1, digits, curStr + c, res) 
                
        