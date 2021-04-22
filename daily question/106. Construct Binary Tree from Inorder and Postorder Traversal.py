# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if inorder:
            rootVal = postorder.pop()
            index = inorder.index(rootVal)
            root = TreeNode(rootVal)
            root.right = self.buildTree(inorder[index + 1:], postorder)
            root.left = self.buildTree(inorder[:index], postorder)
            return root

        return None


