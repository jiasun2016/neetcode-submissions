class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(0, [], nums, res, target)
        return res
    def dfs(self, index, sub, nums, res, target):
        if target == 0:
            res.append(list(sub))
            return
        for i in range(index, len(nums)):
            if target < nums[i]:
                continue 
            sub.append(nums[i])
            self.dfs(i, sub, nums, res, target - nums[i])
            sub.pop()