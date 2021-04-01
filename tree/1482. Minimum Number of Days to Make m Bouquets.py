class Solution:
    # two pointers
    # time complexity O(nlogk) where n is # of flowers and k max-min of bloomDay
    # space complexity O(1)
    def minDays(self, bloomDay, m: int, k: int) -> int:

        def availableBouquets(maxV):
            curK = 0
            curM = 0
            for each in bloomDay:
                if each <= maxV:
                    curK += 1
                    if curK == k:
                        curK = 0
                        curM += 1
                    if curM == m:
                        return True
                else:
                    curK = 0
            return False

        if m * k > len(bloomDay):
            return -1

        left, right = min(bloomDay), max(bloomDay)

        while left <= right:
            mid = left + (right - left) // 2

            if availableBouquets(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
