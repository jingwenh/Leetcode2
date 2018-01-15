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
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        return helper(root.left, root.right);
    }
    
    //返回左子树是不是和右子树对称
    private boolean helper(TreeNode left, TreeNode right) {
        if (left == null && right == null) {
            return true;
        }
        if (left == null || right == null) {
            return false;
        }
        
        boolean isValEqual = (left.val == right.val);
        boolean isSym1 = helper(left.left, right.right);
        boolean isSym2 = helper(left.right, right.left);
        
        return isValEqual && isSym1 && isSym2;
    }
}
