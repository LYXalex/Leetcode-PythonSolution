class Solution:
    # O(n)
    # slide window(特殊，因为所有的单词长度一样)
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        count = Counter(words)
        total = len(words)
        lens = len(words[0])
        ans = []
        for i in range(lens):
            temp = {}
            cnt = 0
            start = i
            for j in range(i, len(s) - lens + 1, lens):
                cur = s[j:j + lens]
                temp[cur] = temp.get(cur, 0) + 1
                cnt += 1
                if cur not in count: count[cur] = 0
                while start <= j and temp[cur] > count[cur]:
                    delete = s[start:start + lens]
                    temp[delete] -= 1
                    start += lens
                    cnt -= 1
                if cnt == total:
                    ans.append(start)
        return ans


