class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # slution for has duplicate 
        visited = [False] * len(nums)
        ans = []
        self.dfs(nums, visited, [], ans)
        return ans
    def dfs(self, nums, visited,sub, ans):
        if len(sub) == len(nums):
            ans.append(list(sub)) 

        for i in range(len(nums)):
            if visited[i]:
                continue 
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue 
            visited[i] = True 
            sub.append(nums[i])
            self.dfs(nums, visited, sub, ans)
            visited[i] = False 
            sub.pop()