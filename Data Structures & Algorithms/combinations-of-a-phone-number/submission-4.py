chars = {
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
        if not digits:
            return []
        res = []
        self.dfs(0, digits, "", res) 
        return res 
    
    def dfs(self, index, digits, subStr, res):
        if len(subStr) == len(digits):
            res.append(subStr) 
            return 
        
        d = digits[index]
        for c in chars[d]:
            self.dfs(index+1, digits, subStr + c, res)
