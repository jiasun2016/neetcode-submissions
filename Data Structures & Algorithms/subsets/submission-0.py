class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        self.dfs(0, nums, [], res) 
        return res

    def dfs(self, index, nums, curr, res):
        if index == len(nums):
            res.append(list(curr))
            return 
        curr.append(nums[index]) 
        self.dfs(index+1, nums, curr, res)
        curr.pop() 
        self.dfs(index+1, nums, curr, res)