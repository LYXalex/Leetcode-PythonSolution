# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        def findnext(node):
            while node.left:
                node = node.left
            return node.val

        if not root: return
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif not root.right:
            return root.left
        elif not root.left:
            return root.right
        else:
            root.val = findnext(root.right)
            root.right = self.deleteNode(root.right, root.val)
        return root





