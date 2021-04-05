# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def helper(root):
            if not root:
                valList.append('x')
            else:
                valList.append(str(root.val))

                helper(root.left)
                helper(root.right)

        valList = []
        helper(root)
        return ','.join(valList)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        if not data:
            return None

        def helper():
            if self.pointer == len(data) or data[self.pointer] == 'x':
                self.pointer += 1
                return None
            root = TreeNode(int(data[self.pointer]))
            self.pointer += 1
            root.left = helper()
            root.right = helper()
            return root

        self.pointer = 0
        return helper()

    def serialize_dfs(self, root):
        if root is None:
            return ''

        def dfs(root_node):
            if root_node is None:
                nodes.append('n')
                return
            nodes.append(str(root_node.val))
            dfs(root_node.left)
            dfs(root_node.right)

        if root is None:
            return ''
        nodes = []
        dfs(root)
        return ','.join(nodes)

    def deserialize_dfs(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        nodes = data.split(',')

        def dfs():
            if nodes[cur_pos[0]] == 'n':
                cur_pos[0] += 1
                return None
            root = TreeNode(int(nodes[cur_pos[0]]))
            cur_pos[0] += 1
            root.left = dfs()
            root.right = dfs()
            return root

        cur_pos = [0]
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


