class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.dfs(nums, 0, [], res)
        return res
    def dfs(self, nums, i, sub, res):
        # if i == len(nums):
        res.append(list(sub)) 
        for i in range(i, len(nums)):
            # self.dfs(nums, i+1, sub, res)
            sub.append(nums[i])
            self.dfs(nums, i+1, sub,res)
            sub.pop()