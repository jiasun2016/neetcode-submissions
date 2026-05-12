class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            sub = [] 
            lens = len(res)
            for i in range(lens):
                sub.append(res[i] + [num])
            res = res + sub
        return res 
        
    