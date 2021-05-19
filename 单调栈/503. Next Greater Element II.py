class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = list(reversed(nums))
        ans = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            ans[i] = stack[-1] if stack else -1
            stack.append(nums[i])
        return ans
