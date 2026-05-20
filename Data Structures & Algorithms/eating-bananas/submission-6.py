class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) 
        while l + 1 < r:
            mid = l + (r-l)//2 
            if self.isvalid(mid, piles, h):
                r = mid 
            else:
                l = mid 
        if self.isvalid(l, piles, h):
            return l 
        if self.isvalid(r, piles, h):
            return r 
        return -1 
    def isvalid(self, rate, piles, h):
        count = 0 
        for p in piles:
            count += math.ceil(p/rate)
        return count <= h 