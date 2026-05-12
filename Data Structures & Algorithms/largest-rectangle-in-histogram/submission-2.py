class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0 
        maxArea = 0 
        n = len(heights)
        stack = []
        for i in range(n+1):
            value = -1 if i == n else heights[i] 
            while stack and heights[stack[-1]] > value:
                index = stack.pop()
                l = stack[-1] if stack else -1
                w = i - l - 1
                h =  heights[index] 
                maxArea = max(w*h, maxArea) 
            stack.append(i)
        return maxArea