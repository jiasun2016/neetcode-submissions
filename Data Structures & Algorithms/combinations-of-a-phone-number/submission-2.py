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
        if not digits:
            return []
        res = []
        self.dfs(0, digits,"", res)
        return res 

    def dfs(self, index, digits, sub, res):
        if len(sub) == len(digits):
            res.append(sub) 
            return 
        for i in range(index, len(digits)):
            for c in dic[digits[i]]:
                self.dfs(i+1, digits,sub+c,res)
        