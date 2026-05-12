class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0 
        stack = [] 
        maxArea = 0 
        n = len(heights) 
        for i in range(n+1):
            val = heights[i] if i < n else -1 
            while stack and heights[stack[-1]] > val:
                index = stack.pop() 
                h = heights[index]
                l = stack[-1] if stack else -1 
                w = i - l - 1 
                maxArea = max(maxArea, h*w) 
            stack.append(i) 
        return maxArea