class Solution:
    def isValid(self, s: str) -> bool:
        closeToopen = {')' :'(','}' : '{',']':'['}
        stack = []

        for r in s:

            if r in closeToopen:
                if stack and stack[-1] == closeToopen[r]:

                    stack.pop()

                else:
                    return False

            else:
                stack.append(r)

        return True if not stack else False 
        




        