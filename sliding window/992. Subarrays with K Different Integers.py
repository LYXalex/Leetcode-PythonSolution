class Solution:

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMost(k):
            ans, left, map, = 0, 0, {}

            for i, num in enumerate(nums):
                map[num] = map.get(num, 0) + 1  # 进
                while len(map) > k:  # 出
                    map[nums[left]] -= 1
                    if map[nums[left]] == 0: del map[nums[left]]
                    left += 1

                ans += i - left + 1  # 算

            return ans

        return atMost(k) - atMost(k - 1)

