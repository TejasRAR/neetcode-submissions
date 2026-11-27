class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []


        for token in tokens:

            if token == '+':
                stack.append(stack[-1] + stack[-2])
                stack.pop(-2)
                stack.pop(-2)

            elif token == '-':
                 stack.append(stack[-2] - stack[-1])
                 stack.pop(-2)
                 stack.pop(-2)
        
            elif token == '*':
                stack.append(stack[-1] * stack[-2])
                stack.pop(-2)
                stack.pop(-2)

            elif token == '/':
                stack.append(int(stack[-2]/stack[-1]))
                stack.pop(-2)
                stack.pop(-2)

            else:
                stack.append(int(token))

        return stack[-1]
        