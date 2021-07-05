class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid(i, j, board, val):
            for index in range(9):
                if index != i and board[index][j] == val:
                    return False
            for index in range(9):
                if index != j and board[i][index] == val:
                    return False
            iStart, jStart = i // 3 * 3, j // 3 * 3
            for m in range(iStart, iStart + 3):
                for n in range(jStart, jStart + 3):
                    if (m != i or n != j) and board[m][n] == val:
                        return False
            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] != "." and not valid(i, j, board, board[i][j]):
                    return False
        return True
