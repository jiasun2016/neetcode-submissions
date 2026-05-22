class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.que = nums
        self.k = k
        heapq.heapify(self.que)
        while len(self.que)>self.k:
            heapq.heappop(self.que) 

    def add(self, val: int) -> int:
        heapq.heappush(self.que, val)
        while len(self.que)>self.k:
            heapq.heappop(self.que) 
        return self.que[0] 
    

        
