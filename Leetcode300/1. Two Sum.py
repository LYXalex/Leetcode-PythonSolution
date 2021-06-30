class Solution:
    # map
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        remDic = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in remDic:
                return [remDic[rem],i]
            remDic[nums[i]] = i