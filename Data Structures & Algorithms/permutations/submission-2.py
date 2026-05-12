class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs([], nums, res, set())
        return res 
    def dfs(self, sub, nums, res, visited):
        if len(sub) == len(nums):
            res.append(list(sub)) 
            return 
        for n in nums:
            if n not in visited:
                sub.append(n)
                visited.add(n)
                self.dfs(sub, nums, res, visited)
                sub.pop()
                visited.remove(n)