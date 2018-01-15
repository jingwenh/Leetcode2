/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
//生成BST = 中间的数创建节点 + 左边数组创建BST拼到节点左边 + 右边数组创建BST拼到右边
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0) {
            return null;
        }
        
        return helper(nums, 0, nums.length - 1);
    }
    
    private TreeNode helper(int[] nums, int start, int end) {
        if (start > end) {
            return null;
        }
        
        int mid = start + (end - start) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        TreeNode left = helper(nums, start, mid - 1);
        TreeNode right = helper(nums, mid + 1, end);
        
        root.left = left;
        root.right = right;
        
        return root;
        
    }
}
