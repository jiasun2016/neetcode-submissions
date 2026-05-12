class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lens = len(heights) 
        l, r = 0, lens-1 
        res = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r-l) 
            res = max(res, area) 
            if heights[l] >= heights[r]:
                r -= 1 
            else:
                l += 1 
        return res 