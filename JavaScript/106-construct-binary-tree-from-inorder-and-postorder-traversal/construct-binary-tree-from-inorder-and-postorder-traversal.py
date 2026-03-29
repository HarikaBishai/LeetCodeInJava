# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        inorder_map = {val:i for i,val in enumerate(inorder)}
        postorder_index = len(postorder) - 1
        
        def dfs(left, right):
            nonlocal postorder_index
            if left > right:
                return None
            # if(postorder_index < 0): return None
            root_val = postorder[postorder_index]
            mid = inorder_map[root_val]

            root = TreeNode(root_val)
            postorder_index-=1
            root.right = dfs(mid+1, right)
            root.left = dfs(left, mid-1)
            

            return root
        return dfs(0, len(inorder)-1)