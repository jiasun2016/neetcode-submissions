class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s): 
            lastIndex[c] = i 
        ans = []
        size = 0
        end = 0 
        for i, c in enumerate(s): 
            size+= 1
            end = max(end, lastIndex[c]) 
            if end == i:
                ans.append(size) 
                size = 0 
        return ans 
            
