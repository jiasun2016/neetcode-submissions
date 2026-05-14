class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftH = [0] * n
        rightH =  [0] * n
        leftH[0] = height[0]
        for i in range(1, n):
            leftH[i] = max(leftH[i-1], height[i])
        rightH[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            rightH[i] = max(rightH[i+1], height[i]) 
        
        maxAre = 0
        for i in range(n):
            maxAre += min(leftH[i], rightH[i]) - height[i]
        return maxAre
        

