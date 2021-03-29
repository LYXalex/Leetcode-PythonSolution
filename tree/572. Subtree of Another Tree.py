# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def equals(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and equals(node1.left, node2.left) and equals(node1.right, node2.right)

        def traverse(node, t):
            return node and (equals(node, t) or traverse(node.left, t) or traverse(node.right, t))

        return traverse(s, t)


