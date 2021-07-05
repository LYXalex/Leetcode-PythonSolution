class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def valid(i, j, board, val):
            for index in range(9):
                if index != i and board[index][j].isdigit() and int(board[index][j]) == val:
                    return False
            for index in range(9):
                if index != j and board[i][index].isdigit() and int(board[i][index]) == val:
                    return False
            iStart, jStart = i // 3 * 3, j // 3 * 3
            for m in range(iStart, iStart + 3):
                for n in range(jStart, jStart + 3):
                    if (m != i or n != j) and board[m][n].isdigit() and int(board[m][n]) == val:
                        return False
            return True

        def dfs():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for val in range(1, 10):
                            if valid(i, j, board, val):
                                board[i][j] = str(val)
                                if dfs():
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True

        dfs()


