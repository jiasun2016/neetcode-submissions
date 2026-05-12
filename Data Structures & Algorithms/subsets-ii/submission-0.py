class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []
        self.dfs(0, nums, [], res)
        return res
    
    def dfs(self, idx, nums, sub, res):
        res.append(sub.copy()) 

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue 
            sub.append(nums[i]) 
            self.dfs(i+1,nums,sub,res) 
            sub.pop()
        
