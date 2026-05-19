class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        res = []
        self.dfs(nums, target, [], res, 0)
        return res 
    def dfs(self, nums, target, sub, res, index):
        if target == 0:
            res.append(list(sub))
            return 
    
        for i in range(index, len(nums)):
            if nums[i] > target:
                break 
            if i > index and nums[i] == nums[i-1]:
                continue 
            sub.append(nums[i])
            self.dfs(nums, target-nums[i], sub, res, i+1)
            sub.pop()
