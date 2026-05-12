class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]  
        count = collections.defaultdict(int) 
        for n in nums:
            count[n] += 1 
        for key in count.keys():
            freq[count[key]].append(key) 
        res = []
        print(freq)
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 

