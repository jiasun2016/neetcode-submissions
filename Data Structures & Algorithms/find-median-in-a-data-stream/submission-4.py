class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        if self.big and num > self.big[0]:
            heapq.heappush(self.big, num)
        else: 
            heapq.heappush(self.small, -num)
        if len(self.small) > len(self.big) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.big, val)
        elif len(self.big) > len(self.small) + 1:
            val = heapq.heappop(self.big)
            heapq.heappush(self.small, -val)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return -self.small[0]
        if len(self.big) > len(self.small):
            return self.big[0]
        return (-self.small[0] + self.big[0])/2.0
        
        