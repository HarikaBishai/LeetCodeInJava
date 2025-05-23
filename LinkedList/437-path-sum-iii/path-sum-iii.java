/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int pathSum(TreeNode root, int targetSum) {
       if(root == null) return 0;

       int count = countFromNode(root, targetSum);

       count+=pathSum(root.left, targetSum);
       count+=pathSum(root.right, targetSum);
       return count;

    }

    public int countFromNode(TreeNode root, long targetSum) {
        if(root == null) return 0;
        int count = 0;

        if (root.val == targetSum) count=1;
        count+= countFromNode(root.left, targetSum-root.val);
        count+= countFromNode(root.right, targetSum-root.val);
        return count;

      
    }
}