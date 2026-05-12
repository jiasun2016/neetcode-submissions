class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
           
            if stack and (
                (stack[-1] == "(" and s[i] == ")") or
                (stack[-1] == "{" and s[i] == "}") or
                (stack[-1] == "[" and s[i] == "]")
            ):
                stack.pop()
            else:
             
                stack.append(s[i])
                
    
        return not stack
