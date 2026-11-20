class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = ['+', 'D', 'C']
        stack = []


        for r in operations:
            
            if r in ops:
                if r == '+':
                    stack.append(stack[-1] + stack[-2])

                elif r == 'D':
                    stack.append(stack[-1] * 2)

                elif r == 'C':
                    stack.pop()

            else:
                stack.append(int(r))

        return sum(stack)
        

        