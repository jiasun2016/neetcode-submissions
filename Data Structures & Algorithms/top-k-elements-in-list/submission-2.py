class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)] 
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1 
        for num, cnt in count.items():
            freq[cnt].append(num)
        arr = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                arr.append(num)
                if len(arr) == k:
                    return arr
                
        