class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        self.dfs(nums,[], res, visited)
        return res 
    def dfs(self, nums, sub, res, visited):
        if len(sub) == len(nums):
            res.append(list(sub))
        for i in range(len(nums)):
            if nums[i] not in visited:
                visited.add(nums[i])
                sub.append(nums[i])
                self.dfs(nums, sub, res, visited)
                sub.pop()
                visited.remove(nums[i]) 
            

