class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
    
        for token in tokens:
            if token in "+-*/":
                a = int(stack.pop())
                b = int(stack.pop())
                if token == "+":
                    c = b+a
                elif token == "-":
                    c = b-a
                elif token == "*":
                    c = a*b
                elif token == "/":
                    c = int(b/a)
                stack.append(c)
            else:
                stack.append(token)
        return int(stack[0])       