class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        results = [] 
        self.dfs(0, [], nums, results)
        return results 

    def dfs(self, index, sub, nums, results):
        results.append(list(sub)) 
        for i in range(index, len(nums)):
            if i > 0 and nums[i] == nums[i-1] and i > index:
                continue
            sub.append(nums[i])
            self.dfs(i+1, sub, nums, results)
            sub.pop()
