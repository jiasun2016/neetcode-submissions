class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        self.dfs(0, target, [], candidates, res)
        return res 
        
    def dfs(self, index, remains, sub, nums, res):
        if remains == 0:
            res.append(list(sub)) 
            return 

        for i in range(index, len(nums)):
            if nums[i] > remains:
                break 
            if i> 0 and nums[i] == nums[i-1] and i > index:
                continue 
            sub.append(nums[i]) 
            self.dfs(i+1, remains - nums[i], sub, nums, res) 
            sub.pop()