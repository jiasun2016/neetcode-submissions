class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"}":"{", "]": "[", ")":"("}
        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False 
        return not stack