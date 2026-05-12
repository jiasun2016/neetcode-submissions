class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)] 
        curr = 0 
        count = 0
        pairs.sort(reverse = True)
        for p, s in pairs:
            if (target - p)/s > curr:
                curr = (target - p)/s
                count += 1 
        return count  
