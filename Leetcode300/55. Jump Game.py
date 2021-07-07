class Solution:
    # greedy
    def canJump(self, nums: List[int]) -> bool:
        cur_cover, last_index = 0, 0
        if len(nums) == 1: return True
        for i in range(len(nums) - 1):
            cur_cover = max(nums[i] + i, cur_cover)
            if cur_cover <= i: return False
        return True

    # greedy
    def canJump(self, nums: List[int]) -> bool:
        last_reach = len(nums) - 1
        if len(nums) == 1: return True
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_reach: last_reach = i
        return last_reach == 0