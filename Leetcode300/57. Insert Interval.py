class Solution:
    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        start,end = newInterval[0],newInterval[1]
        for i,interval in enumerate(intervals):
            if start > interval[1]: new_intervals.append(interval)
            elif interval[0] > end:
                new_intervals.append([start,end])
                new_intervals += intervals[i:]
                break
            else:
                start = min(start,interval[0])
                end = max(end,interval[1])
        if not new_intervals or start > new_intervals[-1][1]:
            new_intervals.append([start,end])
        return new_intervals
