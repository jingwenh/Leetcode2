/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 //中序遍历得到排序数组，然后用一个长度为2的sliding window找到最小差
class Solution {
    public int minDiffInBST(TreeNode root) {
        List<Integer> res = traverse(root);
        int left = 0;
        int right = 1;
        int min = Integer.MAX_VALUE;
        while (right < res.size()) {
            min = Math.min(min, res.get(right) - res.get(left));
            left++;
            right++;
        }
        return min;
    }
    
    private List<Integer> traverse(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        
        res.addAll(traverse(root.left));
        res.add(root.val);
        res.addAll(traverse(root.right));
        
        return res;
    }
}
