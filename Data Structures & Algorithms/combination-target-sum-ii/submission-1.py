class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(0, [], nums, res, target)
        return res
    def dfs(self, index, sub, nums, res, target):
        if target == 0:
            res.append(list(sub))
            return
        for i in range(index, len(nums)):
            if target < nums[i]:
                continue 
            if i > index and nums[i] == nums[i-1]:
                continue
            sub.append(nums[i])
            self.dfs(i+1, sub, nums, res, target - nums[i])
            sub.pop()