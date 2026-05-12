class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)-2):
            target = - nums[i] 
            seen = set()
            for j in range(i+1, len(nums)):
                temp = target - nums[j] 
                if temp in seen:
                    result = sorted([nums[i], temp, nums[j]])
                    if result not in res:
                        res.append(result)
                    
                else:
                    seen.add(nums[j])
        return res

        