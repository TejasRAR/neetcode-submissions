class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = ['+', "C", 'D']
        stack = []
        count = 0

        for r in operations:
            if r in ops:
                if r == '+':
                    stack.append(stack[-1] + stack[-2])
                    count += stack[-1]
                elif r == "C":
                    count -= stack[-1]
                    stack.pop()
                elif r == 'D':
                    stack.append(stack[-1] * 2)
                    count += stack[-1]


            else:
                stack.append(int(r))
                count += int(r)

        return count 