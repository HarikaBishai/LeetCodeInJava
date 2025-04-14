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
    private int maxZigZag = 0;
    public int longestZigZag(TreeNode root) {
        if (root == null) return 0;

        dfs(root.left, true, 1);
        dfs(root.right, false, 1);
        return maxZigZag;
    }

    public void dfs(TreeNode root, boolean isLeft,int length) {
        if(root==null) return;
        maxZigZag = Math.max(maxZigZag, length);

        if(isLeft) {
            dfs(root.right, false , length+1  );
            dfs(root.left, true, 1);
        } else {
            dfs(root.left, true , length+1 );
            dfs(root.right, false, 1);

        }
    }
}