# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        rep = defaultdict(int)

        out = []

        def dfs(root):
            if not root:
                return ''
            curr_rep = '(' + dfs(root.left) + ')' + str(root.val) + '(' + dfs(root.right) + ')'
            rep[curr_rep]+=1
            if rep[curr_rep] == 2:
                out.append(root)
            return curr_rep 
        dfs(root)
        return out