class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        for n in nums:
            count[n]+= 1 
        frq = [[] for i in range(len(nums)+1)]
        for key, val in count.items():
            frq[val].append(key)
        res = []
        for i in range(len(frq)-1, 0, -1):
            for v in frq[i]:
                res.append(v)
                if len(res) == k:
                    return res
        return res