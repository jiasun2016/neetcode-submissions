class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        ans = []

        for i in range(len(nums)):
            while que and nums[que[-1]] < nums[i]:
                que.pop()
            que.append(i)
            if i+1 >= k:
                ans.append(nums[que[0]]) 
                if i - que[0] +1>= k:
                     que.popleft()
        return ans 

            
