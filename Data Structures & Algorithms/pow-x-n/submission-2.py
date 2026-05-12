class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0 
        if n == 0:
            return 1 
        if n < 0:
            x = 1/x 
            n = -n 
        power = n 
        res = 1
        while power:
            if power%2 == 1:
                res *= x 
            x *=x 
            power //=2 
        return res 
