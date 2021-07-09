class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])
        heights, ans = [0] * (m + 1), -1
        heights[-1] = -1
        for i in range(n):
            stack = []
            for j in range(m + 1):
                start = j
                if j < m:
                    if matrix[i][j] == "1":
                        heights[j] += 1
                    else:
                        heights[j] = 0
                while stack and heights[j] < stack[-1][0]:
                    height, idx = stack.pop()
                    ans = max((j - idx) * height, ans)
                    start = min(start, idx)
                stack.append((heights[j], start))
        return ans




