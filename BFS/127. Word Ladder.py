class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        queue = deque([(beginWord, 1)])
        seen = set()
        wordDict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                wordDict[word[:i] + '*' + word[i + 1:]].append(word)

        while queue:

            cur, step = queue.popleft()
            for i in range(len(cur)):
                nextW = cur[:i] + '*' + cur[i + 1:]
                for word in wordDict[nextW]:
                    if word == endWord:
                        return step + 1
                    if word not in seen:
                        seen.add(word)
                        queue.append((word, step + 1))

        return 0




