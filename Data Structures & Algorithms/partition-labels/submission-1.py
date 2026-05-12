class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for index, c in enumerate(s):
            lastIndex[c] = index 
        ans = []
        size = 0
        end = 0
        for index, c in enumerate(s): 
            size += 1
            end = max(end, lastIndex[c])
            if end == index:
                ans.append(size) 
                size = 0
        return ans

