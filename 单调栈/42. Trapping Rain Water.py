## time complexity: O(n)
## space complexity: O(1)
class Solution:
    # two pointer
    def trap1(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        leftMax = -1
        rightMax = -1
        ans = 0
        while left < right:
            if height[left] >= height[right]:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    ans = ans + (rightMax - height[right])
                right -= 1
            else:
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    ans = ans + (leftMax - height[left])
                left += 1

        return ans

    ## using stack  O(n) O(n)
    def trap(self, height: List[int]) -> int:

        stack, ans = [], 0
        for i, each in enumerate(height):
            while stack and each > height[stack[-1]]:
                bottom = height[stack.pop()]

                if stack:
                    ans += (min(height[stack[-1]], each) - bottom) * (i - stack[-1] - 1)

            stack.append(i)

        return ans

    ## dp
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        left = [0] * len(height)
        right = [0] * len(height)
        left[0] = height[0]
        right[-1] = height[-1]
        res = 0
        for i in range(1, len(height)):
            left[i] = max(left[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        for i in range(len(height)):
            res += min(left[i], right[i]) - height[i]
        return res


