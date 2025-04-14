/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    private Map<TreeNode, TreeNode> map = new HashMap<>();

    public  void getParentMap(TreeNode root) {
        if(root==null) return;
        if(root.left!=null) {
            map.put(root.left, root);
            getParentMap(root.left);
        }
        if(root.right!=null) {
            map.put(root.right, root);
            getParentMap(root.right);
        }


    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

        
        if (root == null) return null;
        map.put(root, null);
        getParentMap(root);

        TreeNode curr = p;

        Set<TreeNode> pset = new HashSet<>();
        while(curr!=null) {
            pset.add(curr);
            curr = map.get(curr);
        }

        curr = q;

        while(curr!=null) {
            if(pset.contains(curr)) {
                return curr;
            }
            curr = map.get(curr);
        }
        return null;
    }
}