class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for r in tokens:
         

            if r == '+':

                stack.append(stack.pop() + stack.pop())

            elif r == '-':

                a = stack.pop()
                b = stack.pop()

                stack.append(b - a)


            elif r == '*':

                stack.append(stack.pop() * stack.pop())

            elif r == '/':
                a = stack.pop()
                b = stack.pop()

                stack.append(int(b/a))

            else:
                stack.append(int(r))


        return stack[0]