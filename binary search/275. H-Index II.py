class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n == 0: return 0
        low = 0;
        high = n
        while high > low:
            mid = (low + high) // 2
            if n - mid == citations[mid]:
                return n - mid
            if n - mid > citations[mid]:
                low = mid + 1
            else:
                high = mid
        return n - low
