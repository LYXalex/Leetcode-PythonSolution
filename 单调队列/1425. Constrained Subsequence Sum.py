class Solution:

    ## TLE time complexity O(kn)
    def constrainedSubsetSum1(self, nums: List[int], k: int) -> int:
        # dp[i] = max(nums[i],max(dp[i-j])+nums[i]) where 1<=j<=k
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i]
            for j in range(i - 1, i - k - 1, -1):
                if j >= 0:
                    dp[i] = max(dp[i], dp[j] + nums[i])
        return max(dp)

    ## 因为我们要对比前k个dp里面最大的，我们可以用单调队列来进行记录
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

        dp = [0] * len(nums)
        queue = deque()
        for i in range(0, len(nums)):
            dp[i] = nums[i]
            if queue: dp[i] = max(dp[i], dp[i] + dp[queue[0]])
            ## 保持 k-1 个size
            while queue and i - queue[0] >= k:
                queue.popleft()
            ## 保持递减
            while queue and dp[i] >= dp[queue[-1]]:
                queue.pop()
            ## 加cur
            queue.append(i)
        return max(dp)

#  public int ConstrainedSubsetSum(int[] nums, int k)
#         {
#             int[] dp = new int[nums.Length];
#             dp[0] = nums[0];
#             int currentMaxIndex = 0;
#             for (int j = 1; j < nums.Length; j++)
#             {
#                 if (j - currentMaxIndex > k)
#                 {
#                     currentMaxIndex = j - 1;
#                     for (int i = j - 2; i >= 0 && j - i <= k; i--)
#                         if (dp[currentMaxIndex] < dp[i])
#                             currentMaxIndex = i;
#                 }

#                 dp[j] = Math.Max(nums[j], nums[j] + dp[currentMaxIndex]);

#                 if (dp[currentMaxIndex] < dp[j])
#                     currentMaxIndex = j;
#             }

#             return dp.Max();
#         }