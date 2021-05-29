class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        dsu, map = DSU(len(nums)), {}
        for i, num in enumerate(nums):
            if num in map: continue
            map[num] = i
            if num + 1 in map: dsu.union(i, map[num + 1])
            if num - 1 in map: dsu.union(i, map[num - 1])
        return dsu.getMaxSize()


class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.gSize = [1] * size

    def find(self, x):
        if x != self.parent[x]: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, s1, s2):
        r1, r2 = self.find(s1), self.find(s2)
        if r1 == r2: return
        if self.rank[r1] > self.rank[r2]:
            self.parent[r2] = r1
            self.gSize[r1] += self.gSize[r2]
        elif self.rank[r1] < self.rank[r2]:
            self.parent[r1] = r2
            self.gSize[r2] += self.gSize[r1]
        elif self.rank[r1] == self.rank[r2]:
            self.parent[r1] = r2
            self.rank[r2] += 1
            self.gSize[r2] += self.gSize[r1]

    def getMaxSize(self):
        if not self.gSize: return 0
        return max(self.gSize)

