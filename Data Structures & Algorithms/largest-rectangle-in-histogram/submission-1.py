class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        i = 0 
        maxArea = 0
        stack = []
        for i in range(len(heights)+1):
            while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
                preIndex = stack.pop() 
                width = i- stack[-1]-1 if stack else i
                maxArea = max(maxArea, heights[preIndex] * width)
            stack.append(i)
            i += 1  
        return maxArea
        

