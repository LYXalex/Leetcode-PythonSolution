# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    ## using dictionary
    def recoverFromPreorder1(self, S: str) -> TreeNode:

        treeDict, depth, curVal = {-1: TreeNode(-1)}, 0, ''

        for char in S + '-':
            if curVal and char == '-':
                parent, child = treeDict[depth - 1], TreeNode(int(curVal))
                if not parent.left:
                    parent.left = child
                else:
                    parent.right = child
                treeDict[depth] = child
                depth, curVal = 1, ''

            elif char == '-':
                depth += 1
            else:
                curVal += char
        return treeDict[-1].left

    ## using DFS
    def recoverFromPreorder(self, S: str) -> TreeNode:
        self.index = 0

        def dfs(depth):
            if self.index >= len(S):
                return

            for i in range(depth):
                if S[self.index + i] != '-':
                    return

            self.index += depth
            val = ''
            while self.index < len(S) and S[self.index].isdigit():
                val += S[self.index]
                self.index += 1
            node = TreeNode(int(val))
            node.left = dfs(depth + 1)
            node.right = dfs(depth + 1)

            return node

        return dfs(0)




