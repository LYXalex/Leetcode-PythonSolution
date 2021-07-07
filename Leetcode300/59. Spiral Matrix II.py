class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        iStart, jStart, iEnd, jEnd, idx = 0, 0, n - 1, n - 1, 1
        while iStart <= iEnd and jStart <= jEnd:
            for j in range(jStart, jEnd + 1):
                matrix[iStart][j] = idx
                idx += 1
            iStart += 1

            for i in range(iStart, iEnd + 1):
                matrix[i][jEnd] = idx
                idx += 1
            jEnd -= 1
            if iStart <= iEnd:
                for j in range(jEnd, jStart - 1, -1):
                    matrix[iEnd][j] = idx
                    idx += 1
            iEnd -= 1
            if jStart <= jEnd:
                for i in range(iEnd, iStart - 1, -1):
                    matrix[i][jStart] = idx
                    idx += 1
            jStart += 1

        return matrix





