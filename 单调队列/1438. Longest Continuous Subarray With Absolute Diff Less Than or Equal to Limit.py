class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        maxd, mind = deque([]), deque([])
        ans, left = 0, 0
        for i, num in enumerate(nums):

            while maxd and num > maxd[-1]: maxd.pop()
            while mind and num < mind[-1]: mind.pop()
            maxd.append(num)
            mind.append(num)
            while maxd[0] - mind[0] > limit:
                if maxd[0] == nums[left]: maxd.popleft()
                if mind[0] == nums[left]: mind.popleft()
                left += 1
            ans = max(ans, i - left + 1)
        return ans


