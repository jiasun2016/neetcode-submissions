class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "" 
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s 
        return ans 

    def decode(self, s: str) -> List[str]:
        if not s:
            return [] 
        i = 0 
        ans = []
        while i < len(s):
            j = i 
            while s[j]!= "#":
                j += 1 
            lens = int(s[i:j]) 
            i = j+1 
            j = i + lens 
            ans.append(s[i:j]) 
            i = j 
        return ans 
