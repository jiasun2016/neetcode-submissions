class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1 
        feq = [[] for i in range(len(nums)+1)] 

        for num, cnt in count.items():
            feq[cnt].append(num)  
        
        res = [] 
        for i in range(len(feq)-1, -1, -1):
            nums = feq[i] 
            for num in nums:
                res.append(num) 
                if len(res) == k:
                    return res 
        return res 
