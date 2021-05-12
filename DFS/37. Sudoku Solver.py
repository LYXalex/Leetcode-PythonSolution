class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isValid(board, i, j, num):
            for m in range(9):
                if board[i][m].isdigit() and int(board[i][m]) == num:
                    return False
                if board[m][j].isdigit() and int(board[m][j]) == num:
                    return False
            startI, startJ = (i // 3) * 3, (j // 3) * 3
            for m in range(startI, startI + 3):
                for n in range(startJ, startJ + 3):
                    if board[m][n].isdigit() and int(board[m][n]) == num:
                        return False
            return True

        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for n in range(1, 10):
                            if isValid(board, i, j, n):
                                board[i][j] = str(n)
                                if dfs(board):
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True

        return dfs(board)



