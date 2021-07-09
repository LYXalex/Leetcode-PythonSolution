class Solution:
    # dfs
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        n, m = len(board), len(board[0])

        def dfs(i, j, idx, visited):
            found = False
            if idx == len(word):
                return True

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dir in directions:
                newI, newJ = dir[0] + i, dir[1] + j
                if 0 <= newI < n and 0 <= newJ < m and board[newI][newJ] == word[idx] and (newI, newJ) not in visited:
                    visited.add((newI, newJ))
                    found = found or dfs(newI, newJ, idx + 1, visited)
                    visited.remove((newI, newJ))
            return found

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(i, j, 1, visited): return True
                    visited.remove((i, j))
        return False
