class Solution:
    # two pointer
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r, lMax, rMax, ans = 0, len(height) - 1, height[0], height[-1], 0
        while l <= r:
            if lMax <= rMax:
                # print("l",lMax,height[l])
                if lMax >= height[l]:
                    ans += lMax - height[l]
                else:
                    lMax = height[l]
                l += 1
            else:
                # print("r",rMax,height[r])
                if rMax >= height[r]:
                    ans += rMax - height[r]
                else:
                    rMax = height[r]
                r -= 1
        return ans

    # 扫描线
    def trap1(self, height: List[int]) -> int:

        curL, maxH = -1, [0] * len(height)
        for i in range(len(height)):
            curL = max(curL, height[i])
            maxH[i] = curL
        ans, curR = 0, -1
        for i in range(len(height) - 1, -1, -1):
            curR = max(curR, height[i])
            ans += min(maxH[i], curR) - height[i]

        return ans