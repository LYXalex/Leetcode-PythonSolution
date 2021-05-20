class Solution:
    def removeDuplicateLetters1(self, s: str) -> str:

        count = Counter(s)
        stack = []
        for each in s:
            if each not in stack:
                while stack and count[stack[-1]] > 0 and each < stack[-1]:
                    stack.pop()

                stack.append(each)
            count[each] -= 1
        return ''.join(stack)