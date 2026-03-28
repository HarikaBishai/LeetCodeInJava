# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        maxcount = 0
        if not root:
            return 0

        def dfs(root):
            nonlocal maxcount
            if not root:
                return 0
            
            left_len = dfs(root.left)
            right_len = dfs(root.right)
            
            left_path = 0
            right_path = 0
            if root.left and root.left.val == root.val:
                left_path = left_len + 1
            if root.right and root.right.val == root.val:
                right_path = right_len + 1

            maxcount = max(maxcount, left_path + right_path)
            return max(left_path, right_path)
        
        dfs(root)
        return maxcount