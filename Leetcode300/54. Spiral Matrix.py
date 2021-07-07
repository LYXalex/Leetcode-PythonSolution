class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n, m = len(matrix), len(matrix[0])

        def level(x):
            for j in range(x, m - x):
                ans.append(matrix[x][j])
                # print("1",ans)
            if m - x > x:
                for i in range(x + 1, n - x):
                    ans.append(matrix[i][m - x - 1])
                    # print("2",ans)
                if n - x > x + 1:
                    for j in range(m - x - 2, x - 1, -1):
                        ans.append(matrix[n - x - 1][j])
                        # print(n,x,j)
                    if m - x - 2 > x - 1:
                        for i in range(n - x - 2, x, -1):
                            ans.append(matrix[i][x])
                            # print("4",ans)

        for i in range((n + 1) // 2):
            level(i)
        return ans

    def spiralOrder(self, matrix):
        ret = []
        while matrix:
            ret += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            if matrix:
                ret += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret

