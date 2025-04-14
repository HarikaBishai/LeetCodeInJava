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
    public List<Integer> rightSideView(TreeNode root) {

        List<Integer> out = new ArrayList<>();
        if(root == null) return out;
        Queue<TreeNode> q = new LinkedList<>();

        q.offer(root);

        while(!q.isEmpty()) {
            int length = q.size();
            for(int i=0;i<length;i++) {
                TreeNode node = q.poll();
                if(i == 0) {
                    out.add(node.val);
                }

                if(node.right!=null) {
                    q.offer(node.right);
                }

                if(node.left!=null) {
                    q.offer(node.left);
                }
                
            }
        }

        return out;


    }
}