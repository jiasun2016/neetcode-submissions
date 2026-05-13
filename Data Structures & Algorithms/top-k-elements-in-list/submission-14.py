class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        for n in nums:
            count[n] += 1 
        seen = [[] for i in range(len(nums)+1)]
        for key, v in count.items():
            seen[v].append(key) 
        res = []
        for i in range(len(seen)-1, 0, -1):
            for n in seen[i]:
                res.append(n)
                if len(res) == k:
                    return res 