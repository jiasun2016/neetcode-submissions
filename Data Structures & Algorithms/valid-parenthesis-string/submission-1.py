class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        stars = []
        for i, c in enumerate(s):
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
        return not left