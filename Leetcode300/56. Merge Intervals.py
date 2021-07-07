class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if len(intervals) == 1: return intervals
        start, end, ans = intervals[0][0], intervals[0][1], []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                ans.append([start, end])
                start, end = intervals[i][0], intervals[i][1]
        if not ans or start > ans[-1][1]: ans.append([start, end])
        return ans
