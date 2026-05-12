class Solution:
    def climbStairs(self, n: int) -> int:
        # 如果只有 1 或 2 阶，走法数就是 n 本身
        if n <= 2:
            return n
        # pre2： dp[i-2]：到前两阶的方法数
        # pre1： dp[i-1]：到前一阶的方法数
        pre2, pre1 = 1, 2 
        for i in range(3, n+1):
            # 当前阶的方法数 = 前一阶 + 前两阶
            curr = pre1 + pre2
            # 状态整体向前移动一阶
            pre2 = pre1 # 原 dp[i-1] 变成新的 dp[i-2]
            pre1 = curr # 当前结果变成新的 dp[i-1]
        # dp[n]  
        return pre1 


        