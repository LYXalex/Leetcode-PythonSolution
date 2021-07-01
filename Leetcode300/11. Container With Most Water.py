class Solution:
    # two pointer
    # since area is breadth * height
    # using two pointer let breadth decreasing, the only way to increasing area is to find the higher height
    def maxArea(self, height: List[int]) -> int:
        i, j, maxA = 0, len(height) - 1, 0
        while i < j:
            cur = (j - i) * min(height[i], height[j])
            maxA = max(maxA, cur)
            if height[i] > height[j]:
                j -= 1
            elif height[i] < height[j]:
                i += 1
            else:
                i += 1
                j -= 1
        return maxA
