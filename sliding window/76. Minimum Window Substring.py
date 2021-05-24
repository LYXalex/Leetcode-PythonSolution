class Solution:
    def minWindow(self, s: str, t: str) -> str:

        dicT = Counter(t)
        dicS = {}
        curL, left, visited = len(s) + 1, 0, set()
        start, end = -1, -1
        for i, char in enumerate(s):
            dicS[char] = dicS.get(char, 0) + 1

            if char in dicT and dicS[char] >= dicT[char]:
                visited.add(char)

                while len(visited) == len(dicT):
                    dicS[s[left]] -= 1
                    ## 如果去掉 left就不符合答案，所以left是当前最短的左边界
                    if s[left] in dicT and dicT[s[left]] > dicS[s[left]]:
                        visited.remove(s[left])
                        if i - left + 1 < curL:
                            start, end, curL = left, i, i - left + 1
                    left += 1
        return s[start:end + 1] if curL != len(s) + 1 else ""












