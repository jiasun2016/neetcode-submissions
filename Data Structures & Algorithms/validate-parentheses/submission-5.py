class Solution:
    def isValid(self, s: str) -> bool:
        hash = {')':'(', '}':'{', ']':'['} 
        i = 0
        stack=[]
        while i < len(s):
            if s[i] == "(" or s[i] == "{" or  s[i] == "[":
                stack.append(s[i]) 
            else:
                if stack and stack[-1] == hash[s[i]]:
                    stack.pop() 
                else:
                    return False 
            i += 1 
        return not stack



