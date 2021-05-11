class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        self.ans = []
        nums = [i for i in range(1, n + 1)]

        def dfs(cur, nums):
            if len(nums) + len(cur) < k:
                return
            if len(cur) == k:
                self.ans.append(cur)
                return

            for i, num in enumerate(nums):
                dfs(cur + [num], nums[i + 1:])

        dfs([], nums)
        return self.ans