class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.dfs(0, [], nums, res)
        return res
    def dfs(self, start, sub, nums, res):
        res.append(list(sub))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            sub.append(nums[i])
            self.dfs(i+1,sub, nums,res) 
            sub.pop()