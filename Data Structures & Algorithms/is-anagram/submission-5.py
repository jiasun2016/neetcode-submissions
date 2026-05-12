class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False 
        seen = {} 
        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]] += 1 
            else:
                seen[s[i]] = 1 
        for i in range(len(t)): 
            if t[i] not in seen or seen[t[i]] == 0:
                return False 
            if t[i] in seen and seen[t[i]]> 0:
                seen[t[i]] -= 1 
        for key in seen:
            if seen[key] != 0:
                return False 
        return True
            