class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[[]]
        for num in nums: 
            newsets = []
            for sub in res:
                newsets.append(sub + [num])
            res = res + newsets
        return res 
        