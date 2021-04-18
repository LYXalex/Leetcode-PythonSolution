# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def findFrequentTreeSum(self, root: TreeNode):
        sumDict = collections.defaultdict(int)

        def getSum(node):
            if not node:
                return 0
            left = getSum(node.left)
            right = getSum(node.right)
            sumDict[node.val + left + right] += 1

            return node.val + left + right

        getSum(root)

        ans = []
        if not sumDict:
            return ans
        maxV = max(sumDict.values())

        return [k for k, v in sumDict.items() if v == maxV]


