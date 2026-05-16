class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        stack = []

        for r in range(len(nums)):
            while stack and nums[stack[-1]] < nums[r]:
                stack.pop()
            stack.append(r)
            if r + 1 >= k:
                ans.append(nums[stack[0]])  
            if r - stack[0] + 1 >= k:
                stack.pop(0)
        return ans 

