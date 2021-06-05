# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    import math
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def dfs(node, ans):
            if not node: return
            ans.append(str(node.val))
            dfs(node.left, ans)
            dfs(node.right, ans)

        ans = []
        dfs(root, ans)
        return " ".join(ans)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        dataList = data.split(" ")
        if len(dataList[0]) == 0: return []

        def helper(dataList, minV, maxV):
            if not dataList: return None
            if minV < int(dataList[0]) < maxV:
                cur = int(dataList.pop(0))
                root = TreeNode(cur)
                root.left = helper(dataList, minV, cur)
                root.right = helper(dataList, cur, maxV)

                return root

        minV, maxV = -math.inf, math.inf
        return helper(dataList, minV, maxV)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans