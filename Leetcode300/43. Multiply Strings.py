class Solution:

    def multiply1(self, num1: str, num2: str) -> str:
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

    # 大数乘法的算法
    def multiply(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        ans = [0] * (m + n)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                p1, p2 = i + j, i + j + 1
                sum = mul + ans[p2]

                ans[p2] = sum % 10
                ans[p1] += sum // 10
        ans = "".join(map(str, ans))
        return '0' if not ans.lstrip('0') else ans.lstrip('0')
