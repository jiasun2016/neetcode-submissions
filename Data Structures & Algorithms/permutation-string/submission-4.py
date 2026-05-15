class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        count1 = {}
        count2 = {}
        for i in range(len(s1)):
            count1[s1[i]] = count1.get(s1[i], 0) + 1
            count2[s2[i]] = count2.get(s2[i], 0) + 1

        needs = len(count1)
        has = 0
        for c in count1:
            if count2.get(c) == count1[c]:
                has += 1
        
        if has == needs: return True

        l = 0
        for r in range(len(s1), len(s2)):
            char_r = s2[r]
            char_l = s2[l]

            if char_r in count1:
                if count2.get(char_r, 0) == count1[char_r]:
                    has -= 1
                
                count2[char_r] = count2.get(char_r, 0) + 1
                
                if count2[char_r] == count1[char_r]:
                    has += 1
            else:
                count2[char_r] = count2.get(char_r, 0) + 1

            if char_l in count1:
                if count2.get(char_l, 0) == count1[char_l]:
                    has -= 1
                count2[char_l] -= 1
                if count2[char_l] == count1[char_l]:
                    has += 1
            else:
                count2[char_l] -= 1
            l += 1
            # 每一轮滑动结束，只需要 O(1) 的判断
            if has == needs:
                return True
        return False