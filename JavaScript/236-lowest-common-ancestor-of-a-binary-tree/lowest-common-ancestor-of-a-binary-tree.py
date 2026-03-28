# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parentObj = {root: None}

        def getParentObj(root):
            if not root:
                return 
            if root.left:
                parentObj[root.left] = root
            if root.right:
                parentObj[root.right] = root
            getParentObj(root.left)
            getParentObj(root.right)

        getParentObj(root)
        pathSetP = set() 
        while p:
            pathSetP.add(p)
            p = parentObj[p]

        while q and q not in pathSetP:
            q =  parentObj[q]
        return q