class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freq = new Map()
        for(const num of nums){
            freq.set(num, (freq.get(num)?? 0) + 1)
        }
        const arr = Array.from({length: nums.length+1}, () => [])
        for(const [num, cnt] of freq.entries()){
            arr[cnt].push(num)
        }
        const res = []
        for(let i = arr.length-1; i>= 0; i --){
            for(const n of arr[i]){
                res.push(n)
                if(res.length === k) return res
            }
        }
    }
}
