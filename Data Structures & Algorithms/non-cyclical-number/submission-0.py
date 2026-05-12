class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set() 
        while n not in visited:
            visited.add(n) 
            n = self.getSumOfSquare(n)
            if n == 1:
                return True 
        return False

    def getSumOfSquare (self, n):
        ans = 0 
        while n:
            temp = n%10 
            temp *= temp 
            ans+= temp 
            n = n//10  
        return ans

