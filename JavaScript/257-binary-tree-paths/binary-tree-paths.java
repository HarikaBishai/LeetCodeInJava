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

    List<String> out = new ArrayList<>();
    public List<String> binaryTreePaths(TreeNode root) {
        getPath(root, "");
        return out;
    }

    public void getPath(TreeNode root, String path) {
        if(root == null) {
            return;
        }

        path +=  root.val;
       
        if(root.left==null && root.right==null) {
            out.add(path);
            return;
        }

        
        getPath(root.left,path + "->" );
        getPath(root.right,path + "->" );
        
    }
}