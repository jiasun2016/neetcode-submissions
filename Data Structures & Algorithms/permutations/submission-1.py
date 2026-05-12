class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False]*len(nums)
        self.dfs(nums, [], res, visited)
        return res 
        
    def dfs(self, nums, sub, res, visited):
        if len(sub) == len(nums):
            res.append(sub.copy()) 
        for i in range(len(nums)):
            if visited[i]== True:
                continue 
            visited[i] = True
            sub.append(nums[i]) 
            self.dfs(nums, sub, res, visited) 
            sub.pop()
            visited[i] = False
        
