class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        ans = []
        self.dfs(0, 0, [], ans, n)
        return ans
    def dfs(self, left, right, sub, ans, n):
        if left == right == n:
            ans.append("".join(sub))
            return 
        if left < n:
            sub.append("(")
            self.dfs(left + 1, right, sub, ans, n)
            sub.pop()
        if left > right:
            sub.append(")")
            self.dfs(left, right+1, sub, ans, n)
            sub.pop()
