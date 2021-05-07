class Solution:
    def insert(self, intervals, newInterval) :

        # edge case
        if not intervals: return [newInterval]
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        if newInterval[0] > intervals[len(intervals) - 1][1]:
            intervals.append(newInterval)
            return intervals

        res = []
        for interval in intervals:
            if not newInterval or newInterval[0] > interval[1]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                res.append(interval)
                newInterval = None
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        if newInterval: res.append(newInterval)

        return res
