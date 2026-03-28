# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        minStr = None
        path = []


        def dfs(root, currStr):
            nonlocal minStr
            if not root:
                return
            currStr = chr(ord('a') +root.val)+currStr

            if not root.left and not root.right:
                
                if minStr is None or currStr < minStr:
                    minStr = currStr
                return
            
            dfs(root.left, currStr)
            dfs(root.right, currStr)
        dfs(root,'')
        return minStr

