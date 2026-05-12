class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(0, 0, [], res, n)
        return res
    def dfs(self, left, right, sub, res, n):
        if left == right == n:
            res.append("".join(list(sub)))
        if left > n:
            return 

        sub.append("(")
        self.dfs(left+1, right, sub, res, n)
        sub.pop()
        if left > right:
            sub.append(")")
            self.dfs(left, right+1, sub, res, n)
            sub.pop()