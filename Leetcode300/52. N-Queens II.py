class Solution:
    def totalNQueens(self, n: int) -> int:
        def check(point, curs):
            for cur in curs:
                if cur[1] == point[1]: return False
                if abs(cur[1] - point[1]) == abs(cur[0] - point[0]): return False
            return True

        self.ans = 0

        def dfs(level, curs):
            if level == n:
                self.ans += 1
                return

            for i in range(n):
                if check((level, i), curs):
                    curs.append((level, i))
                    dfs(level + 1, curs)
                    curs.pop()

        dfs(0, [])
        return self.ans