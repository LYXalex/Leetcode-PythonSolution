class Solution:

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        presum = [0] * (len(nums) + 1)
        for i in range(len(nums)): presum[i + 1] = presum[i] + nums[i]
        ## here sum from i to j-1 is presum[j] - presum[i] j > i
        ## we keep presum[i] part in queue
        ans, queue = len(nums) + 1, deque([])
        for i in range(len(nums) + 1):
            while queue and presum[i] - presum[queue[0]] >= k:
                ans = min(ans, i - queue.popleft())
            while queue and presum[queue[-1]] >= presum[i]:
                queue.pop()
            queue.append(i)
        return ans if ans != len(nums) + 1 else -1




