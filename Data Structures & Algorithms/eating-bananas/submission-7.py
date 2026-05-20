class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) 
        while l < r:
            mid = l + (r-l)//2 
            if self.isvalid(mid, piles, h):
                r = mid 
            else:
                l = mid +1
        return l
    def isvalid(self, rate, piles, h):
        count = 0 
        for p in piles:
            count += math.ceil(p/rate)
        return count <= h 