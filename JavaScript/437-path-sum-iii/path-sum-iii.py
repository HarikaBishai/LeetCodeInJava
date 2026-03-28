# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        prefixSum = defaultdict(int)
        prefixSum[0] = 1

        def dfs(root, currSum):
            if not root:
                return 0
            
            currSum += root.val
            
            count = prefixSum[currSum-targetSum]
            prefixSum[currSum] +=1
            count+=dfs(root.left, currSum)
            count+=dfs(root.right, currSum)
            prefixSum[currSum] -=1

            return count
        if not root:
            return 0
        return  dfs(root, 0)