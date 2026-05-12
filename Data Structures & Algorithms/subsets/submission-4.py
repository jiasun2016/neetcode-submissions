class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(0, [], nums, res)
        return res 

    def dfs(self, index, sub, nums, res):
        res.append(list(sub))
        for i in range(index, len(nums)):
            sub.append(nums[i])
            self.dfs(i+1, sub, nums, res)
            sub.pop()
        

        