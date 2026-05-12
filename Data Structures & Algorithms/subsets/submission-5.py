class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(0, [], nums, res)
        return res 

    def dfs(self, index, sub, nums, res):
        if index == len(nums):
            res.append(list(sub))
            return
        
        self.dfs(index+1, sub, nums, res)
        sub.append(nums[index])
        self.dfs(index+1, sub, nums, res)
        sub.pop()

        