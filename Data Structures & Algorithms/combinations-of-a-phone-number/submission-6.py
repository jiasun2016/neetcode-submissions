dics = {
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
        ans = []
        self.dfs(digits, 0, [], ans)
        return ans 
    def dfs(self, digits, index, sub, ans):
        if index == len(digits):
            ans.append("".join(sub))
            return 
        for c in dics[digits[index]]:
            sub.append(c)
            self.dfs(digits, index+1, sub, ans)
            sub.pop()
        
                    


     