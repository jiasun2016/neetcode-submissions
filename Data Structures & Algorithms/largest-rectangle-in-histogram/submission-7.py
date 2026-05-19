class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxAre = 0
        for i in range(len(heights)+1):
            val = heights[i] if i<len(heights) else -1
            while stack and heights[stack[-1]] > val:
                index = stack.pop()
                h = heights[index] 
                l = stack[-1] if stack else -1 
                w = i - l - 1 
                maxAre = max(maxAre, h*w) 
            stack.append(i) 
        return maxAre
                 
