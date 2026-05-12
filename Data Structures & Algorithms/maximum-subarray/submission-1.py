class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        maxSum, minSum = float("-inf"), 0
        prefixSum = 0
        for num in nums:
            prefixSum += num 
            maxSum = max(maxSum,prefixSum-minSum) 
            minSum = min(minSum, prefixSum) 
        return maxSum
