class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i >= n:
                return i == n #one valid way
            if i not in memo:
                memo[i] = dfs(i+1) + dfs(i+2) 
            return memo[i] 
        return dfs(0)