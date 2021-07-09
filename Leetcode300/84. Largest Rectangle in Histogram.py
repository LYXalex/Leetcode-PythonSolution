class Solution:
    # monotonus stack
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        stack,ans = [],-1
        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][0]:
                height,idx = stack.pop()
                ans = max(ans,(i-idx)*height)
                start = min(idx,start)
            stack.append((heights[i],start))
        return ans