class Solution:
    # solve for subsetII has duplicate
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        end = 0
        for i in range(len(nums)):
            start = 0
            lens = len(res)
            if i > 0 and nums[i] == nums[i-1]:
                start = end + 1 
            end = len(res) - 1 
            for j in range(start,lens):
                res.append(list(res[j]) + [nums[i]])
        return res 
        
    