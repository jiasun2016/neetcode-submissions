class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False 
        a = ord("a")
        counts1, counts2 = [0]*26, [0]*26
        for i in range(len(s1)):
            counts1[ord(s1[i]) - a] += 1 
            counts2[ord(s2[i]) - a] += 1
        match = 0
        for i in range(26):
            if counts1[i] == counts2[i]:
                match += 1 
        l = 0
        for r in range(len(s1), len(s2)):
            if match == 26:
                return True 
            indexR = ord(s2[r]) - a 
            indexL = ord(s2[l]) - a 
            counts2[indexR] += 1
            if counts1[indexR] == counts2[indexR]:
                match += 1
            elif counts1[indexR] + 1 == counts2[indexR]:
                match -= 1 
            counts2[indexL] -= 1
            if counts1[indexL] == counts2[indexL]:
                match += 1
            elif counts1[indexL] - 1 == counts2[indexL]:
                match -= 1
            l += 1 
        return match == 26


            
            