class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        que = []
        for n in nums:
            heapq.heappush(que, n)
            if len(que) > k:
                heapq.heappop(que)
        return heapq.heappop(que)