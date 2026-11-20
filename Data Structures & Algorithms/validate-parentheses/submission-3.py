class Solution:
    def isValid(self, s: str) -> bool:
        count = {'}' : '{', ']' : '[', ')' : '('}
        stack = []

        for r in s:

            if r in count:
                if stack and stack[-1] == count[r]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(r)

        return True if not stack else False
        