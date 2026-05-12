class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const seen = {}
        for(let i =0; i < nums.length; i ++){
            if(seen[target - nums[i]] !== undefined){
                return [seen[target - nums[i]], i]
            }
            seen[nums[i]] = i
        }
        return [-1, -1]
    }
}
