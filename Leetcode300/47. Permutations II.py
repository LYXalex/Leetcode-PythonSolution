class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(nums, cur):
            if not nums:
                ans.append(cur)
                return

            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    dfs(nums[:i] + nums[i + 1:], cur + [nums[i]])

        dfs(nums, [])
        return ans