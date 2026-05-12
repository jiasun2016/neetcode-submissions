class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 
        lens = len(height) 
        res = 0 
        maxLefts = self.getMaxLeft(height)
        maxRights = self.getMaxRight(height) 
        for i in range(lens):
            res += min(maxLefts[i], maxRights[i]) - height[i] 
        return res 
    
    def getMaxLeft(self, height):
        res = [] 
        maxL = -float('inf')
        for i in range(len(height)):
            maxL = max(maxL, height[i]) 
            res.append(maxL) 
        return res 

    def getMaxRight(self, height):
        res = [] 
        maxR = -float('inf') 
        for i in range(len(height)-1, -1, -1):
            maxR = max(height[i], maxR)
            res.append(maxR) 
        return res[::-1] 


        