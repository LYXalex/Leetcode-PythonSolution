class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def dfs(curWord, trieNode, x, y):
            if trieNode.isWord: self.ans.add(curWord)

            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dir in directions:
                if 0 <= x + dir[0] < len(board) and 0 <= y + dir[1] < len(board[0]) and board[x + dir[0]][
                    y + dir[1]] in trieNode.children:
                    temp = board[x + dir[0]][y + dir[1]]
                    board[x + dir[0]][y + dir[1]] = '#'
                    dfs(curWord + temp, trieNode.children[temp], x + dir[0], y + dir[1])
                    board[x + dir[0]][y + dir[1]] = temp

        wordTrie = Trie()
        for word in words:
            wordTrie.addWord(word)
        curWord = ''
        self.ans = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in wordTrie.children:
                    tmp = board[i][j]
                    board[i][j] = '#'
                    dfs(tmp, wordTrie.children[tmp], i, j)
                    board[i][j] = tmp
        return self.ans


class Trie:
    def __init__(self):
        self.isWord = False
        self.children = {}

    def addWord(self, word):

        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.isWord = True

    def searchWord(self, word):
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isWord

    def searchPrefix(self, prefix):
        node = self
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True






