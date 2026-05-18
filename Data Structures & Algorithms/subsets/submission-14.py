class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = [[]]
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                start = end + 1 
            else:
                start = 0 
            end = len(res)
            for j in range(start, end):
                newSub = res[j]
                res.append(newSub + [nums[i]])
        return res 
