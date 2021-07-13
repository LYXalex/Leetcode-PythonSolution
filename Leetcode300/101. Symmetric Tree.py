# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive
    def isSymmetric1(self, root: TreeNode) -> bool:

        def helper(l, r):
            if not l and not r: return True
            if not l or not r: return False
            return l.val == r.val and helper(l.left, r.right) and helper(l.right, r.left)

        if not root: return True
        return helper(root.left, root.right)

    # iterative
    def isSymmetric(self, root: TreeNode) -> bool:

        leftS, rightS = [root.left], [root.right]
        while leftS and rightS:
            l = leftS.pop()
            r = rightS.pop()

            if (not l and r) or (not r and l): return False
            if r and l:
                if l.val != r.val: return False
                leftS.append(l.left)
                leftS.append(l.right)
                rightS.append(r.right)
                rightS.append(r.left)
        if rightS or leftS: return False
        return True
