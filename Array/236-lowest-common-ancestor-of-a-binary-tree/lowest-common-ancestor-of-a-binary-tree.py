# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        parent_map = {root: None}
        def getParentMap(node, parent):
            if node:
                if node.left:
                    parent_map[node.left] = node
                    getParentMap(node.left, node)
                if node.right:
                    parent_map[node.right] = node
                    getParentMap(node.right, node)
        
        getParentMap(root, None)

        path_nodes_p = set()

        curr = p
        while curr:
            path_nodes_p.add(curr)
            curr = parent_map[curr]
        
        curr = q
        while curr and curr not in path_nodes_p:
            curr = parent_map[curr]
        
        return curr


