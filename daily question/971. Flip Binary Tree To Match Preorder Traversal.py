# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage) :

        def flipped(node):
            if not node:
                return
            if node and not voyage:
                self.ans = [-1]
                return

            if node.val != voyage.pop(0):
                self.ans = [-1]
                return

            # flipped
            if voyage and node.left and node.left.val != voyage[0]:
                self.ans.append(node.val)
                flipped(node.right)
                flipped(node.left)
            else:
                flipped(node.left)
                flipped(node.right)

        self.ans = []
        flipped(root)
        if self.ans and self.ans[0] == -1:
            self.ans = [-1]
        return self.ans




