class Solution:
    import math
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if k > len(nums):
            return []
        queue, ans = deque([]), [0] * (len(nums) - k + 1)
        for i, num in enumerate(nums):
            startWindow = i - k + 1
            ## keep the window size to k-1
            while queue and i - queue[0] >= k:
                queue.popleft()
            ## check inscreasing in queue
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            ## add the cur element
            queue.append(i)
            ## calculate the current ans
            if startWindow >= 0:
                ans[startWindow] = nums[queue[0]]
        return ans
