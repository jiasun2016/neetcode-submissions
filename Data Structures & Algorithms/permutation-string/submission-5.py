class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        a = ord("a")
        count1 = [0] * 26
        count2 = [0] * 26
        for i in range(len(s1)):
            count1[ord(s1[i])-a] += 1
            count2[ord(s2[i])-a] += 1
        has = 0
        for i in range(26):
            if count1[i] == count2[i]:
                has += 1 
        if has == 26:
            return True 
        l = 0
        for r in range(len(s1), len(s2)):
            if has == 26:
                return True 
            indexL = ord(s2[l]) - a 
            indexR = ord(s2[r]) - a 
            count2[indexR] += 1 
            if count2[indexR] == count1[indexR]:
                has += 1
            elif count2[indexR]-1 == count1[indexR]:
                has -= 1
            count2[indexL] -= 1
            if count2[indexL] == count1[indexL]:
                has += 1 
            elif count2[indexL] + 1 == count1[indexL]:
                has -= 1 
            l += 1 
        return has == 26 

