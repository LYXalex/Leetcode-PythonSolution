class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(nums, cur):
            ans.append(cur[:])
            if not nums: return

            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    cur.append(nums[i])
                    dfs(nums[i + 1:], cur)
                    cur.pop()

        dfs(nums, [])
        return ans