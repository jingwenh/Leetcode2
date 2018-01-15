/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    /*
     * @param root: The root of binary tree.
     * @return: True if the binary tree is BST, or false
     */
     //isValidBST
         //1. 左边最大值小于root.val，并且左边是BST
         //2. 右边最小值大于root.val，并且右边是BST
     //Recursion:
        //Param: root
        //return: isBST, min, max
        
    //两个坑：
    //1. 初始化min和max用的是整数的最大和最小值，但是测试的时候有case是Integer.MAX_VALUE，这种情况和min比较会出现等于返回false; 因此不能判断是BST的情况，而是判断不是BST的情况
    //2. 不能在一边为空的时候做比较
    public boolean isValidBST(TreeNode root) {
        return helper(root).isBST;
    }
    
    private class ResultType {
        int min;
        int max;
        boolean isBST;
        ResultType(int min, int max, boolean isBST) {
            this.min = min;
            this.max = max;
            this.isBST = isBST;
        }
    }
    
    private ResultType helper(TreeNode root) {
        if (root == null) {
            return new ResultType(Integer.MAX_VALUE, Integer.MIN_VALUE, true);
        }
        
        ResultType leftRT = helper(root.left);
        ResultType rightRT = helper(root.right);
        
        boolean isBST = true;
        
        if (!leftRT.isBST) {
            return new ResultType(0,0, false);
        }
        if (!rightRT.isBST) {
            return new ResultType(0,0, false);
        }        
        if (root.left != null && root.val <= leftRT.max) {//不能在一边为空的时候做比较
            return new ResultType(0,0, false);
        }
        if (root.right != null && root.val >= rightRT.min) {//不能在一边为空的时候做比较
            return new ResultType(0,0, false);
        }        
        
        int min = root.val;
        if (min > leftRT.min) {
            min = leftRT.min;
        }
        if (min > rightRT.min) {
            min = rightRT.min;
        }
        
        int max = root.val;
        if (max < leftRT.max) {
            min = leftRT.max;
        }
        if (max < rightRT.max) {
            max = rightRT.max;
        }
        
        return new ResultType(min, max, isBST);
    }
    
    
}
