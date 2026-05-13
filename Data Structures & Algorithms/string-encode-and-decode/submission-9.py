class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for s in strs:
            lens = len(s)
            res += str(lens) + "#" + s
        return res 

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i = 0
        res = []
        while i < len(s):
            j = i 
            while s[j]!= "#":
                j += 1 
            lens = int(s[i:j]) 
            i = j + 1 
            j = i + lens 
            res.append(s[i:j])
            i = j 
        return res 

