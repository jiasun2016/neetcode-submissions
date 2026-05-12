class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque([])
       
        ans = []
        for r in range(len(nums)):
            curr = nums[r]
            while stack and nums[stack[-1]] < curr:
                stack.pop()
            stack.append(r)
            if r+1 >= k:
                ans.append(nums[stack[0]]) 
            if stack[0] < r-k+2:
                stack.popleft()
        return ans
