class Solution:
    def merge(self, intervals):
        res = []
        if not intervals:
            return res

        intervals.sort()
        first = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] > first[1]:
                res.append(first)
                first = intervals[i]
            else:
                first = [first[0], max(first[1], intervals[i][1])]

        res.append(first)
        return res



