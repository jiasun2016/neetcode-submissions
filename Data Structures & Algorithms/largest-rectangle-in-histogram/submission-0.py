class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0 
        
        for i in range(len(heights)+1):
            while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                maxArea = max(maxArea, width * height)
            stack.append(i)
        return maxArea