class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [ (p, s) for p, s in zip(position, speed)]  
        pair.sort(reverse = True) 
        count = 0 
        curr = 0
        for p, s in pair: 
            time = (target- p)/s 
            if time > curr:
                curr = time 
                count += 1 
        return count
