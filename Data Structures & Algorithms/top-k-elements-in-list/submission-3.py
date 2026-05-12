class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1 
        heap = [] 
        for num, cnt in count.items():
            heapq.heappush(heap, [cnt, num]) 
            if len(heap) > k:
                heapq.heappop(heap) 
        ans = []
        while len(ans) < k:
            ans.append(heapq.heappop(heap)[1]) 
        return ans
