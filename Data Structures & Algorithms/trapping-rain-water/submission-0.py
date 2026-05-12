class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 
        lens = len(height)
        leftMax, rightMax = height[0], height[lens-1] 
        l, r = 0, lens-1
        res = 0
        while l < r: 
            if height[l] < height[r]:
                l += 1 
                leftMax = max(height[l], leftMax)
                res += leftMax - height[l] 
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                res += rightMax - height[r]  
        return res
