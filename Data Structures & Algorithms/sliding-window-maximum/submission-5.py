class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque([])
       
        ans = []
        for r in range(len(nums)):
            curr = nums[r]
            while stack and nums[stack[-1]] < curr:
                stack.pop()
            stack.append(r)
            if stack[0] + k == r:
                stack.popleft()
            if r+1 >= k:
                ans.append(nums[stack[0]]) 
        return ans
