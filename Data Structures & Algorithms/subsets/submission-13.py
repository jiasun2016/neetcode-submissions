class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = [[]]
        
        for num in nums:
            lens = len(res)
            for i in range(lens):
                newSub = res[i]
                res.append(newSub + [num])
        return res 
