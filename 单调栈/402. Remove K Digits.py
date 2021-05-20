class Solution:

    def removeKdigits(self, num: str, k: int) -> str:

        if k >= len(num): return '0'
        curK, stack = 0, []

        for each in num:
            while curK < k and stack and each < stack[-1]:
                stack.pop()
                curK += 1
            stack.append(each)
            ## delete less than k elements
        if curK < k: stack = stack[:len(stack) - k + curK]

        ## remove the leading zero
        return str(int(''.join(stack)))

