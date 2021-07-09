class Solution:
    # dfs
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []

        def dfs(nums, num, cur):
            if num == k:
                ans.append(cur)
                return

            if len(nums) < k - num: return

            for i in range(len(nums)):
                dfs(nums[i + 1:], num + 1, cur + [nums[i]])

        nums = [i + 1 for i in range(n)]
        dfs(nums, 0, [])
        return ans