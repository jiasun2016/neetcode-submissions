class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums.sort()
        self.dfs(0, nums, [], target, results) 
        return results
        
    def dfs(self, index, nums, sub, res, results):
        if res == 0:
            results.append(list(sub))
            return  
        if res < 0:
            return 
        for i in range(index, len(nums)):
            if nums[i] > res:   
                break
            sub.append(nums[i])
            self.dfs(i, nums, sub, res- nums[i], results)
            sub.pop() 
            