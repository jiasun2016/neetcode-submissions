class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = ["+", "-", "*", "/"]
        stack = []
        for c in tokens:
            if c not in signs:
                stack.append(int(c))
            else: 
                temp1 = stack.pop() 
                temp2 = stack.pop()  
                if c == "+":
                    temp = temp1 + temp2 
                elif c == "*":
                    temp = temp1 * temp2 
                elif c == "-":
                    temp = temp2 - temp1
                elif c == "/":
                    temp = int(temp2 / temp1) 
                stack.append(temp) 
        return stack[-1]

