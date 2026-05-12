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
        res = [""]
        for d in digits:
            newRes = []
            for subStr in res:
                for c in chars[d]: 
                    newRes.append(subStr + c)
            res = newRes 
        return res

                