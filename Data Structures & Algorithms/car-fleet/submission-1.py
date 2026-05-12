class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse = True) 
        res = 0 
        curr = 0
        for p, s in pair:
            time = (target-p)/s 
            if curr < time:
                res += 1 
                curr = time
        return res
