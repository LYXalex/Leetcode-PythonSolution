class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = "0"
        for i in range(len(num2) - 1, -1, -1):
            one, carryIn, level = int(num2[i]), 0, ""
            for j in range(len(num1) - 1, -1, -1):
                carryIn += one * int(num1[j])
                level = str(carryIn % 10) + level
                carryIn = carryIn // 10
            level = str(carryIn) + level
            level += "0" * (len(num2) - 1 - i)
            ans = str(int(ans) + int(level))
        return ans

