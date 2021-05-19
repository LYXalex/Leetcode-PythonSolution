class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        temp = {}
        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            temp[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])

        ans = []
        for num in nums1:
            ans.append(temp[num])
        return ans


