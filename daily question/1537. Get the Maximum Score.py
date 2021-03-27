class Solution:
    ## greedy solution with two pointer
    def maxSum(self, nums1, nums2) -> int:
        pointer1, pointer2, ans = 0, 0, 0
        sum1, sum2, overflow = 0, 0, 10 ** 9 + 7

        while pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums1[pointer1] < nums2[pointer2]:
                sum1 += nums1[pointer1]
                pointer1 += 1
            elif nums1[pointer1] > nums2[pointer2]:
                sum2 += nums2[pointer2]
                pointer2 += 1
            ## meet same number choose current max path
            else:
                ans += max(sum1, sum2) + nums1[pointer1]
                sum1, sum2 = 0, 0
                pointer1 += 1
                pointer2 += 1

        if pointer1 < len(nums1):
            sum1 += sum(nums1[pointer1:])
        if pointer2 < len(nums2):
            sum2 += sum(nums2[pointer2:])
        return (max(sum1, sum2) + ans) % overflow




