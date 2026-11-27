class Solution:
    def isValid(self, s: str) -> bool:
        ops = {'}' : '{', ')' : '(', ']' : '['}
        stack = []

        for r in s:

            if r in ops:
                if stack and stack[-1] == ops[r]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(r)

        return True if not stack else False 
        
        