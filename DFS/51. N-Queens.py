class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        line = ""
        for i in range(n):
            line += '.'

        board = []
        for i in range(n):
            board.append(line)

        def isValid(board, i, j):
            for p in range(n):
                for q in range(n):
                    if board[p][q] == 'Q' and (p == i or q == j or (p - i) == (q - j) or (p + q) == (i + j)):
                        return False

            return True

        self.ans = []

        def dfs(board, level):
            if level == n:
                self.ans.append(board[:])
                return
            for i in range(n):
                if isValid(board, level, i):
                    board[level] = board[level][:i] + 'Q' + board[level][i + 1:]
                    dfs(board, level + 1)
                    board[level] = board[level][:i] + '.' + board[level][i + 1:]

        dfs(board, 0)
        return self.ans


