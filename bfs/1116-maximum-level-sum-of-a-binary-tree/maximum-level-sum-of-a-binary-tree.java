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
    public int maxLevelSum(TreeNode root) {
        if(root==null) return 0;
        long maxSum = Long.MIN_VALUE;
        int row = -1;

        Queue<TreeNode> q = new LinkedList<>();

        q.offer(root);

        int currRow = 1;
        while(!q.isEmpty()) {
            long currSum = 0;
            int length = q.size();
            for(int i=0;i<length;i++) {
                TreeNode node = q.poll();
                currSum+=node.val;

                if(node.left!=null) {
                    q.offer(node.left);
                }
                if(node.right!=null) {
                    q.offer(node.right);
                }
            }

            if(currSum > maxSum) {
                maxSum = currSum;
                row = currRow;
            }
            System.out.println(currSum);
            currRow++;
        }

        return row;
    }
}