class TrieNode:
    def __init__(self):
        self.val = -1
        self.children = {}


class Trie:
    def __init__(self, length):
        self.root = TrieNode()
        self.len = length

    def addNum(self, num):
        node = self.root
        for i in range(self.len, -1, -1):
            val = 1 if (1 << i) & num else 0
            if val not in node.children:
                node.children[val] = TrieNode()
            node = node.children[val]
        node.val = num


class Solution:

    def findMaximumXOR(self, nums: List[int]) -> int:
        maxL = len(bin(max(nums))) - 2
        numTries = Trie(maxL)
        for num in nums: numTries.addNum(num)
        ans = 0
        for num in nums:
            node = numTries.root
            for i in range(maxL, -1, -1):
                val = 1 if (1 << i) & num else 0
                node = node.children[1 - val] if 1 - val in node.children else node.children[val]

            ans = max(ans, node.val ^ num)
        return ans



