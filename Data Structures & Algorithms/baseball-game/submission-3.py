class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = ['+', "C", 'D']
        stack = []

        for r in operations:
            if r in ops:
                if r == '+':
                    stack.append(stack[-1] + stack[-2])
                elif r == 'C':
                    stack.pop()
                elif r == 'D':
                    stack.append(stack[-1] * 2)



            else:
                stack.append(int(r))

        return sum(stack) 
        