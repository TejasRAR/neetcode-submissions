class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ops = ['+','D','C']
        count = 0

        for r in operations:

            if r in ops:
                if stack and r == '+':
                    stack.append(int(stack[-1] + stack[-2]))

                elif stack and r == 'C':
                    stack.pop()
                     
                elif stack and r == 'D':
                    stack.append(int(stack[-1]) * 2)


            else:
                stack.append(int(r))

            

        return sum(stack)