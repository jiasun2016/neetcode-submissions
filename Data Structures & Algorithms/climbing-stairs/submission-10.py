class Solution:
    def climbStairs(self, n: int) -> int:
        pre1, pre2 = 1, 1 
        if n == 0:
            return 0 
        if n == 1:
            return 1

        for i in range(2,n+1):
            curr = pre1+ pre2
            pre1 = pre2
            pre2 = curr
        return curr