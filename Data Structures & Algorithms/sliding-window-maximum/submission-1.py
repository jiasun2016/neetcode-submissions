class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = [] 
        ans = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]]< nums[i]:
                stack.pop()
            stack.append(i)
            if stack[0] + k == i:
                stack.pop(0)
            if i >= k-1: 
                ans.append(nums[stack[0]]) 
        return ans
            