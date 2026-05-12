class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 
        res = 0 
        maxLeft = self.getMaxfromleft(height)
        maxRight = self.getMaxfromright(height)
        for i in range(len(height)):
            res += min(maxLeft[i], maxRight[i]) - height[i] 
        return res 
    
    def getMaxfromleft(self, height):
        res = [] 
        maxHeight = 0
        for i in range(len(height)):
            maxHeight = max(maxHeight, height[i]) 
            res.append(maxHeight) 
        return res 

    def getMaxfromright(self, height):
        res = [] 
        maxH = 0 
        for i in range(len(height)-1, -1, -1): 
            maxH = max(maxH, height[i])
            res.append(maxH) 

        return res[::-1]




