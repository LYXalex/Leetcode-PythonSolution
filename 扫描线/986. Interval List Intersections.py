class Solution:
    def intervalIntersection(self, firstList, secondList) :
        m, n, p1, p2, ans = len(firstList), len(secondList), 0, 0, []

        while p1 < m and p2 < n:
            left = max(firstList[p1][0], secondList[p2][0])
            right = min(firstList[p1][1], secondList[p2][1])
            if right >= left:
                ans.append([left, right])

            if firstList[p1][1] <= secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return ans

