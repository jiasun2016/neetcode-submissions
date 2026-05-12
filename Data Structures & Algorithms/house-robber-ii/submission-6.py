class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {}
        def dfs(i, rob0):
            if i >= len(nums) or (rob0 and i == len(nums) - 1):
                return 0
            if (i, rob0) not in memo:
                memo[(i, rob0)] = max(nums[i]+ dfs(i+2, rob0), dfs(i+1, rob0)) 
            return memo[(i, rob0)]
        return max(dfs(0, True), dfs(1, False))

