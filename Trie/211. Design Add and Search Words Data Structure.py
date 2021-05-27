class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWord = False
        self.children = {}

    def addWord(self, word: str) -> None:
        # words = [word]
        # for i in range(len(word)):
        #     words.append(word[:i]+'.'+word[i+1:])
        # print(words)
        # for each in words:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary()
            node = node.children[char]
        node.isWord = True

    def search(self, word: str) -> bool:

        def helper(pos, node):
            if pos == len(word): return node.isWord
            if word[pos] != '.': return word[pos] in node.children and helper(pos + 1, node.children[word[pos]])

            for char in node.children:
                if helper(pos + 1, node.children[char]):
                    return True
            return False

        node = self
        return helper(0, node)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)