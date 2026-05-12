class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs([], nums, res, set())
        return res 
    def dfs(self, sub, nums, res, visited):
        if len(sub) == len(nums):
            res.append(list(sub)) 
            return 
        for i in range(len(nums)):
            n = nums[i]
            if i > 0 and n == nums[i-1] and n not in visited:
                continue 
            if n not in visited:
                sub.append(n)
                visited.add(n)
                self.dfs(sub, nums, res, visited)
                sub.pop()
                visited.remove(n)