class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse = True) 
        count, curr = 0, 0
        for p, s in pairs: 
            time = (target-p)/s 
            if time > curr: 
                count+= 1 
                curr = time 
        return count 