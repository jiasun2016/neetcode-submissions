class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        visited = set() 
        self.dfs(visited, nums, [], results)
        return results
        
    def dfs(self, visited, nums, sub, results):
        if len(sub) == len(nums):
            results.append(sub.copy()) 
            return 

        for num in nums:
            if num in visited:
                continue 
            visited.add(num)
            sub.append(num) 
            self.dfs(visited, nums, sub, results) 
            sub.pop()
            visited.remove(num)