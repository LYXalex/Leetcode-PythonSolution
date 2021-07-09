class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l < r:
            mid = l + r >> 1
            val = matrix[mid // m][mid % m]
            if val >= target:
                r = mid
            else:
                l = mid + 1
        return matrix[l // m][l % m] == target


