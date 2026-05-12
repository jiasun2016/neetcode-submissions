class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 
        maxFromL = self.getMaxFromL(height) 
        maxFromR = self.getMaxFromR(height)
        ans = 0  
        for i in range(len(height)):
            ans += min(maxFromL[i], maxFromR[i]) - height[i] 
        return ans 
    def getMaxFromL(self, height):
        ans = [] 
        maxH = height[0]
        for i in range(len(height)):
            maxH = max(maxH,height[i])
            ans.append(maxH) 
        return ans
    def getMaxFromR(self,height):
        ans = [] 
        maxH = height[-1] 
        for i in range(len(height)-1, -1, -1):
            maxH = max(maxH,height[i])
            ans.append(maxH) 
        return ans[::-1]


