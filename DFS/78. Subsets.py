class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        def dfs(cur, index):
            self.ans.append(cur[:])

            for i in range(index, len(nums)):
                cur.append(nums[i])
                dfs(cur, i + 1)
                cur.remove(nums[i])

        dfs([], 0)
        return self.ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        def dfs(cur, nums):
            self.ans.append(cur)

            for i, num in enumerate(nums):
                dfs(cur + [num], nums[i + 1:])

        dfs([], nums)
        return self.ans

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     # n = len(nums)
    #     # rightEnd = 2**n
    #     # res = []
    #     # for number in range(rightEnd):
    #     #     ans = []
    #     #     for bit in range(n):
    #     #         print(number,bit,1<<bit)
    #     #         if 1<<bit & number:
    #     #             ans.append(nums[bit])
    #     #     res.append(ans)
    #     # return res
    #     print(5 >> 2)