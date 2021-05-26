class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def atMost(k):
            left, ans, curOdd = 0, 0, 0

            for i, num in enumerate(nums):
                if num % 2 == 1: curOdd += 1
                while curOdd > k:
                    if nums[left] % 2 == 1: curOdd -= 1
                    left += 1
                ans += i - left + 1
            return ans

        return atMost(k) - atMost(k - 1)