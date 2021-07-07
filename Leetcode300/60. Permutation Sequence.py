class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans, nums = "", [str(i + 1) for i in range(n)]
        factorial = [0] * (n + 1)
        factorial[0] = 1
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i
        k -= 1
        for i in range(1, n + 1):
            index = k // factorial[n - i]
            ans += nums[index]
            nums.pop(index)
            k -= index * (factorial[n - i])
        return ans


def getPermutation1(self, n: int, k: int) -> str:
    ans = ''
    nums = list(map(str, range(1, n + 1)))
    fact = math.factorial(len(nums) - 1)
    k -= 1
    while k:
        i, k = divmod(k, fact)
        ans += nums.pop(i)
        fact //= len(nums)
    ans += ''.join(nums)
    return ans