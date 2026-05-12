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
        if index >= len(nums) or nums[index] > res:
            return 
       
        sub.append(nums[index])
        self.dfs(index, nums, sub, res- nums[index], results)
        sub.pop() 
        self.dfs(index+1, nums, sub, res, results)