class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        dsu = DSU(m)
        for i in range(m):
            for j in range(m):
                if isConnected[i][j] == 1:
                    dsu.union(i, j)

        return dsu.curS


class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.curS = size

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, s1, s2):
        root1, root2 = self.find(s1), self.find(s2)
        if root1 == root2: return
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] == self.rank[root2]:
            self.parent[root2] = root1
            self.rank[root1] += 1
        self.curS -= 1