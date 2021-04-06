# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if inorder:
            rootVal = preorder.pop(0)
            index = inorder.index(rootVal)
            root = TreeNode(rootVal)
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index + 1:])

            return root
        return None