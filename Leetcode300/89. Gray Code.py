class Solution:
    # 找规律
    def grayCode1(self, n: int) -> List[int]:

        res = [0]
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] + (1 << i))
        return res

    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range(1 << n):
            res.append(i ^ i >> 1)
        return res
