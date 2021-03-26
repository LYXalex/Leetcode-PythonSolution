## time complexity: O(nlogn) for sorting, O(n) worst case for adding up, total O(nlogn)
## space complexity: O(1)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        ans = 0
        overflow = 10 ** 9 + 7

        nums.sort()

        while start <= end:
            if 2 * nums[start] > target:
                break
            if nums[start] + nums[end] > target:
                end -= 1
            else:
                ans += 2 ** (end - start)
                start += 1
        return ans % overflow