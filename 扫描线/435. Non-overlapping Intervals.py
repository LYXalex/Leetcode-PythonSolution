class Solution:

    def eraseOverlapIntervals(self, intervals) -> int:
        if len(intervals) <= 1:
            return 0
        intervals = sorted(intervals, key=lambda x: (x[1], x[0]))
        curEnd = intervals[0][1]
        ans = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < curEnd:
                ans += 1
            else:
                curEnd = intervals[i][1]
        return ans
