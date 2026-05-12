class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        ans = []
        for r in range(len(nums)):
            curr = nums[r]
            # 维护单调递减队列
            # 如果当前元素比队尾对应的元素大，
            # 队尾元素永远不可能再成为窗口最大值，直接弹出
            while stack and nums[stack[-1]] < curr:
                stack.pop()
            stack.append(r)
            # 当窗口大小达到 k 时，记录当前窗口最大值
            # 当前窗口range [r - k + 1, r]
            if r + 1 >= k:
                ans.append(nums[stack[0]])
            # 4. 如果队头元素已经滑出窗口，则移除
            # 窗口左边界是 r - k + 1
            if stack[0] <= r - k + 1:
                stack.popleft()
        return ans 