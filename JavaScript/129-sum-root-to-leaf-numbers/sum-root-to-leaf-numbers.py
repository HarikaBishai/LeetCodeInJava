# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        out = 0

        def dfs(root, curr):
            nonlocal out
            if not root:
                return 0
            curr = curr*10 + root.val

            if not root.left and not root.right:
                out+= curr
            
            dfs(root.left, curr)
            dfs(root.right, curr)
        dfs(root,0)
        return out
            


