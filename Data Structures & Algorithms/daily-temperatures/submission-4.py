class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        i = 0
        while i < len(temperatures):
            if not stack:
                stack.append(i) 
                i += 1 
            elif temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i) 
                i += 1 
            else:
                preIndex = stack.pop()
                res[preIndex] = i - preIndex
        return res
            

