class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones) 
        while len(stones) > 1:
            first = heapq.heappop(stones) 
            second = heapq.heappop(stones)
            if second > first:
                rest = heapq.heappush(stones, first - second) 
        return abs(stones.pop())if len(stones) > 0 else 0