# class SummaryRanges:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.inputs = []
#         self.curs = []
#         self.intervals = []


#     def addNum(self, val: int) -> None:
#         self.inputs.append(val)
#         self.curs.append(val)
#         return self.inputs

#     def getIntervals(self) -> List[List[int]]:
#         for cur in self.curs:
#             if not self.intervals or cur > self.intervals[len(self.intervals)-1][1]+1:
#                 self.intervals.append([cur,cur])
#             else:
#                 for i,interval in enumerate(self.intervals):
#                     if interval[0]-1 <= cur <= interval[1]+1:
#                         interval[0] = min(interval[0],cur)
#                         interval[1] = max(interval[1],cur)
#                         if i+1 < len(self.intervals) and self.intervals[i+1][0]-1 == interval[1]:
#                             interval[1] = self.intervals[i+1][1]
#                             del self.intervals[i+1]
#                         break
#                     elif cur < interval[0]-1:
#                         self.intervals.insert(i,[cur,cur])
#                         break
#         self.curs = []
#         return self.intervals

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []
        self.seen = set()

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val not in self.seen:
            self.seen.add(val)
            heapq.heappush(self.intervals, [val, val])

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """

        tmp = []

        while self.intervals:
            cur = heapq.heappop(self.intervals)
            if tmp and cur[0] <= tmp[-1][1] + 1:
                tmp[-1][1] = max(tmp[-1][1], cur[1])
            else:
                tmp.append(cur)

        self.intervals = tmp
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()