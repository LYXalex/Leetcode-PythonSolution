# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # recursive
    def zigzagLevelOrder1(self, root: TreeNode) -> List[List[int]]:

        ans, level = [], 0

        def dfs(node, ans, level):
            if not node: return
            if level > len(ans) - 1: ans.append([])
            if level % 2 == 0:
                ans[level].append(node.val)
            else:
                ans[level].insert(0, node.val)
            if node.left: dfs(node.left, ans, level + 1)
            if node.right: dfs(node.right, ans, level + 1)

        dfs(root, ans, level)
        return ans

    # iterative
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        level, ans, stack = 0, [], deque([root])

        while stack:
            size = len(stack)
            level, temp = level + 1, []
            for i in range(size):
                cur = stack.popleft()
                # left to right
                # if len(ans) % 2 == 1:
                if level % 2 == 1:
                    temp.append(cur.val)
                else:
                    temp.insert(0, cur.val)

                if cur.left: stack.append(cur.left)
                if cur.right: stack.append(cur.right)
            ans.append(temp)
        return ans

