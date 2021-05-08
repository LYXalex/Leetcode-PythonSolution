class Solution:
    def removeCoveredIntervals1(self, intervals) -> int:
        unique = []
        for interval in intervals:
            if interval not in unique:
                unique.append(interval)
        sortedInterval = sorted(unique, key=lambda x: (x[0], -x[1]))
        removeSet = set()
        for i in range(len(sortedInterval)):
            for j in range(i + 1, len(sortedInterval)):
                if sortedInterval[j][0] > sortedInterval[i][1]:
                    break
                if (sortedInterval[j][0], sortedInterval[j][1]) not in removeSet and sortedInterval[j][1] <= \
                        sortedInterval[i][1]:
                    removeSet.add((sortedInterval[j][0], sortedInterval[j][1]))
        return len(sortedInterval) - len(removeSet)

    # since we sorted by start time, we only need to care about end time

    def removeCoveredIntervals(self, intervals) -> int:
        cnt, end = 0, -1
        sortedInterval = sorted(intervals, key=lambda x: (x[0], -x[1]))
        for interval in sortedInterval:
            if end < interval[1]:
                cnt += 1
                end = interval[1]
        return cnt

