class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end  = 1, max(piles) 
        while start + 1 < end:
            mid = start + (end - start)//2 
            total = self.getTotal(mid, piles) 
            if total <= h:
                end = mid
            else:
                start = mid 
        if self.getTotal(start, piles)  <= h:
            return start 
        return end 
    def getTotal(self, rate, piles):
        count = 0 
        for p in piles:
            count += math.ceil(p/rate) 
        return count 