# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode):# -> List[str]:

        def dfs(cur, curAns):
            if not cur:
                return

            if not cur.left and not cur.right:
                curAns.append(str(cur.val))
                self.ans.append(("->").join(curAns))

            dfs(cur.left, curAns + [str(cur.val)])
            dfs(cur.right, curAns + [str(cur.val)])

        curAns, self.ans = [], []
        dfs(root, curAns)

        return self.ans
