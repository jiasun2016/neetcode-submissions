class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) + 1 
        freq = []
        for num, cnt in counter.items():
            freq.append([cnt, num])
        freq.sort()  
        res = []
        for i in range(k):
            res.append(freq.pop()[1])
        return res 
