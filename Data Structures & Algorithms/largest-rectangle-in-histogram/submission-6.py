class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxAre = 0 
        for i in range(len(heights)+1):
            val = heights[i] if i < len(heights) else -1 
            while stack and heights[stack[-1]] > val:
                curr = stack.pop()
                h = heights[curr]
                l = stack[-1] if stack else -1 
                maxAre = max(maxAre, (i - l - 1)* h) 
            stack.append(i) 
        return maxAre
