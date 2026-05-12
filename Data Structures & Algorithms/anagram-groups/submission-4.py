class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in seen:
                seen[key].append(s)
            else:
                seen[key] = [s]
        res = []
        for key in seen:
            temp = []
            for val in seen[key]:
                temp.append(val) 
            res.append(temp) 
        return res 