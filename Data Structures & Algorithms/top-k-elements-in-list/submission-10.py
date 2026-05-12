class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        for n in nums:
            count[n] += 1 
        arr = []
        for n, v in count.items():
            arr.append([v, n])
        arr.sort()
        res = []
        while k > min(len(res), len(nums)):
            res.append(arr.pop()[1])
        return res
