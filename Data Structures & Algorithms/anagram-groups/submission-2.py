class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            count = [0]*26 
            for c in s:
                count[ord(c)-ord("a")] += 1 
            if tuple(count) not in dic:
                dic[tuple(count)] = []                   
            dic[tuple(count)].append(s)
        return list(dic.values())
