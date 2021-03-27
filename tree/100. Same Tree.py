# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ## recursion
    ## time complexity: O(n)
    ## space complexity: best O(nlogn) worst O(n)
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if not (p or q):
            return True

        if not (p and q):
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)




