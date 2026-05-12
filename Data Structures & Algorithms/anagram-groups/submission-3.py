class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            sortS = "".join(sorted(s))
            if sortS not in seen:
                seen[sortS] = []
            seen[sortS].append(s)
        return list(seen.values())
                