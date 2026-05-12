class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1 # 第0 阶， # 第一阶
        for i in range(2, n+1):
            one, two = one + two, one

        return one