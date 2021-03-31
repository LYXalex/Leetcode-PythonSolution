# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum1(self, root: TreeNode, sum: int) -> int:

        def dfs(cur, path):
            if not cur:
                return 0

            path.append(cur.val)

            count = 0
            curSum = 0
            for i in range(len(path) - 1, -1, -1):
                curSum += path[i]
                if curSum == sum:
                    count += 1

            count += dfs(cur.left, path)
            count += dfs(cur.right, path)

            path.pop()
            return count

        path = []

        return dfs(root, path)

    def pathSum1(self, root: TreeNode, sum: int) -> int:

        prefix = {0: 1}
        self.ans, curSum = 0, 0

        def dfs(cur, curSum):
            if not cur:
                return
            curSum += cur.val
            self.ans += prefix.get(curSum - sum, 0)
            prefix[curSum] = prefix.get(curSum, 0) + 1
            dfs(cur.left, curSum)
            dfs(cur.right, curSum)

            prefix[curSum] = prefix.get(curSum, 0) - 1

        dfs(root, curSum)
        return self.ans
