class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.dfs(nums, [], res, 0)
        return res 
    
    def dfs(self, nums, sub, res, index):
        res.append(list(sub))
            
        for i in range(index, len(nums)): 
            if i > index and nums[i] == nums[i-1]:
                continue 
            sub.append(nums[i])
            self.dfs(nums, sub, res, i+1)
            sub.pop()