class Solution:
    def largestRectangleArea1(self, heights: List[int]) -> int:
        stack = []
        maxAns = -1
        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                val, index = stack.pop()
                maxAns = max(maxAns, (i - index) * val)
                start = min(start, index)
            stack.append((height, start))

            ## for reaching the end
            if i == len(heights) - 1:
                while stack:
                    val, index = stack.pop()
                    maxAns = max(maxAns, (i - index + 1) * val)

        return maxAns

    ## and a zero to the end to not separately consider the case when reaching the last index
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack, area = [], 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                area = max(area, h * w)
            stack.append(i)
        return area

