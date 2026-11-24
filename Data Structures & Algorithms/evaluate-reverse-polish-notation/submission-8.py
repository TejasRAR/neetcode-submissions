class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        stack = []

        for r in tokens:
        
            if r in ops:
                if stack  and r == '+':
                    stack.append(stack.pop() + stack.pop())
                    #stack.pop(stack[-2])
                    #stack.pop(stack[-2])

                elif stack and r == '-':
                    a,b = stack.pop(),stack.pop()
                    stack.append(b - a)
                    #stack.pop(stack[-2])
                    #stack.pop(stack[-2])

                elif stack and r == '*':
                    stack.append(stack.pop() * stack.pop())
                    #stack.pop(stack[-2])
                    #stack.pop(stack[-2])

                elif stack and r == '/':
                    a, b = stack.pop(),stack.pop()
                    stack.append(int(b/a))
                    #stack.pop(stack[-2])
                    #stack.pop(stack[-2])
            else:
                stack.append(int(r))

        return stack[0]