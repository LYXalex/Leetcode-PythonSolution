# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        # recursion
        def getInorderTraversal1(root, temp):
            if not root: return
            getInorderTraversal(root.left, temp)
            temp.append(root.val)
            getInorderTraversal(root.right, temp)

        # iteration
        def getInorderTraversal(root, temp):
            stack = deque([])
            while root or stack:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                temp.append(root.val)
                root = root.right

        temp = []
        getInorderTraversal(root, temp)

        def build(start, end):
            if start <= end:
                mid = start + (end - start) // 2
                root = TreeNode(temp[mid])
                root.left = build(start, mid - 1)
                root.right = build(mid + 1, end)
                return root

        return build(0, len(temp) - 1)
