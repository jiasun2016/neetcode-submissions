class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = 0 
        que = [-s for s in stones]
        heapq.heapify(que)
        while len(que) >1:
            s1= -heapq.heappop(que)
            s2 = -heapq.heappop(que) 
            if s1 > s2:
                heapq.heappush(que, -(s1-s2)) 
        return -que[0] if que else 0 