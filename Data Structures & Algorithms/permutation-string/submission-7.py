class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        count1 = [0]*26 
        count2 = [0]*26 
        a = ord("a")
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
            
            rIndex = ord(s2[r])-a
            count2[rIndex] += 1
            if count1[rIndex] == count2[rIndex]:
                has += 1 
            elif count1[rIndex] == count2[rIndex]-1:
                has -= 1 
            lIndex = ord(s2[l])-a
            count2[lIndex] -= 1
            if count1[lIndex] == count2[lIndex]:
                has += 1  
            elif count1[lIndex] == count2[lIndex] + 1:
                has -= 1 
            if has == 26:
                return True 
            l += 1 
        return False
