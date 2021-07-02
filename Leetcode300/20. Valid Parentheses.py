class Solution:
    def isValid(self, s: str) -> bool:
        leftValid = ['(', '{', '[']
        rightValid = [')', '}', ']']
        stack = []
        i = 0
        while i < len(s):
            if s[i] in leftValid:
                stack.append(s[i])
            else:
                if not stack or leftValid.index(stack.pop()) != rightValid.index(s[i]):
                    return False
            i += 1
        if stack:
            return False
        return True
