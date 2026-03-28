# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        out = []

        def getPathSumNodes(root, target, path):
            if not root:
                return False
            
            target = target-root.val
            
            
            if target == 0 and not root.left and not root.right:
                out.append(path[:] + [root.val])
                return 
            
            getPathSumNodes(root.left, target, path + [root.val])  
            getPathSumNodes(root.right, target, path + [root.val])
        
        getPathSumNodes(root, targetSum, [])
        return out
