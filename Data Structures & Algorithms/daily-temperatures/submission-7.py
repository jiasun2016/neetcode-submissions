class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sigins = ["+", "-", "*", "/"]
        for t in tokens:
            if t not in sigins:
                stack.append(int(t))
            else:
                n2 = stack.pop() 
                n1 = stack.pop()
                curr = None 
                if t == "+":
                    curr = n1 + n2 
                elif t == "-":
                    curr = n1- n2 
                elif t == "*":
                    curr =n1*n2 
                elif t == "/":
                    curr = int(n1/n2)
                stack.append(curr)
        return stack[0]

