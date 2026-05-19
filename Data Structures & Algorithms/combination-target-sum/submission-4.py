class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, target, [], res)
        return res
    def dfs(self, nums, index, target, sub, res):
        if target == 0:
            res.append(list(sub))
            return 
        if target < 0:
            return 
        for i in range(index, len(nums)):
            sub.append(nums[i])
            self.dfs(nums, i, target - nums[i], sub, res)
            sub.pop()