class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        maxSum, prefixMinSum = float("-inf"), 0
        prefixSum = 0
        for num in nums:
            prefixSum += num 
            maxSum = max(maxSum,prefixSum-prefixMinSum) 
            prefixMinSum = min(prefixMinSum, prefixSum) 
        return maxSum
