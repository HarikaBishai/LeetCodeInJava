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
    public int goodNodes(TreeNode root) {
        
        return getgoodNodes(root, root.val);
        
    }

    public static int getgoodNodes(TreeNode root,int maxValue){
        if (root == null) return 0;
        int count = 0;

        if(root.val >= maxValue) {
            count++;
            maxValue = root.val;
        }
        return count + getgoodNodes(root.left, maxValue) + getgoodNodes(root.right, maxValue);

    }
}