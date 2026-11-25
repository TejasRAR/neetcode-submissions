class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+','-','*','/']
        stack = []

        for r in tokens:

            if r in ops:
                if stack and r == '+':
                    stack.append(stack[-1] + stack[-2])
                    stack.pop(-2)
                    stack.pop(-2)
                elif stack and r == '-':
                    stack.append(stack[-2] - stack[-1])
                    stack.pop(-2)
                    stack.pop(-2)

                elif stack and r == '*':
                    stack.append(stack[-1] * stack[-2])
                    stack.pop(-2)
                    stack.pop(-2)

                elif stack and r == '/':
                    stack.append(int(stack[-2] / stack[-1]))
                    stack.pop(-2)
                    stack.pop(-2)


            else:
                stack.append(int(r))
        
        return stack[0] 
