# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ## iterate
    def levelOrderBottom1(self, root: TreeNode):# -> List[List[int]]:
        if not root:
            return []

        def height(cur):
            if not cur:
                return 0
            return max(height(cur.left), height(cur.right)) + 1

        height = height(root)
        stack, ans = [(root, height - 1)], [[] for _ in range(height)]

        while stack:
            cur, level = stack.pop(0)

            ans[level].append(cur.val)

            if cur.left:
                stack.append((cur.left, level - 1))
            if cur.right:
                stack.append((cur.right, level - 1))
        return ans

        # recursion

    def levelOrderBottom(self, root: TreeNode):# -> List[List[int]]:
        def height(cur):
            if not cur:
                return 0
            return max(height(cur.left), height(cur.right)) + 1

        height = height(root)

        def dfs(cur, ans, level):
            if not cur:
                return
            ans[level].append(cur.val)
            if cur.left:
                dfs(cur.left, ans, level - 1)
            if cur.right:
                dfs(cur.right, ans, level - 1)

        ans = [[] for _ in range(height)]
        dfs(root, ans, height - 1)
        return ans
