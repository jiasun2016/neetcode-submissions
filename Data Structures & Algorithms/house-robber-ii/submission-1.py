class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        if len(nums) <= 2:
            return max(nums) 
        
        n1 = self. helper(nums, 0, len(nums)-1, [0]*3) 
        n2 = self. helper(nums, 1, len(nums), [0]*3) 
        return max(n1, n2)
        

    def helper(self, nums, start, end, dp):
        rob1, rob2 = 0, 0
        for i in range(start, end):
            newRob = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = newRob 
        return rob2 
