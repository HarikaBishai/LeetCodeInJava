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
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<TreeNode> leaf1 = new ArrayList<>();
        List<TreeNode> leaf2 = new ArrayList<>();

        getListNodes(root1, leaf1);
        getListNodes(root2,leaf2);
        
        if(leaf1.size()!=leaf2.size()) return false;

        
        for(int i=0;i<leaf1.size(); i++) {
            if(leaf1.get(i).val!= leaf2.get(i).val) {
                return false;
            }
        }

        return true;
    }

    public static void getListNodes(TreeNode root, List<TreeNode> leafNodes) {
        if (root == null) return;

        if(root.left==null && root.right==null) {
            leafNodes.add(root);
            return;
        } 

        getListNodes(root.left, leafNodes);
        getListNodes(root.right, leafNodes);
        return;
        
    }
}