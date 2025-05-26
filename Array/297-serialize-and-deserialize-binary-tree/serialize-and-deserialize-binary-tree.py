# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        result = []

        def dfs(node):
            if not node:
                result.append("N")
                return 
            
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        preorder = data.split(",")
        i = 0



        def dfs():
            nonlocal i
            if preorder[i] == 'N':
                i+=1
                return None
            node = TreeNode(int(preorder[i]))
            i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        root = dfs()
        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))