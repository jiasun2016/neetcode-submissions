class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = [] 
        self.dfs(0, [], nums, results)
        return results 

    def dfs(self, index, sub, nums, results):
        results.append(list(sub)) 
        for i in range(index, len(nums)):
            sub.append(nums[i])
            self.dfs(i+1, sub, nums, results)
            sub.pop()

