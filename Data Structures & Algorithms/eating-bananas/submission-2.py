class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles) 
        while start + 1 < end:
            mid = start + (end-start)//2 
            total = self.getTotal(piles, mid) 
            if total > h:
                start = mid 
            else:
                end = mid 
        if self.getTotal(piles, start) <= h:
            return start 
        else:
            return end  
    def getTotal(self, piles, rate):
        time = 0
        for p in piles:
            time += math.ceil(p / rate)
        return time 
    

