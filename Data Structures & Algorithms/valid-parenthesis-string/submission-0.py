class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []  
        stars = [] 
        n = len(s)
        for i in range(n):
            c = s[i] 
            if c == "(":
                left.append(i) 
            elif c == "*":
                stars.append(i)
            else: 
                if left:
                    left.pop() 
                elif stars:
                    stars.pop() 
                else:
                    return False  
        
        while left and stars:
            leftIndex = left.pop() 
            starIndex = stars.pop() 
            if leftIndex > starIndex:
                return False 
        return len(left) == 0

                