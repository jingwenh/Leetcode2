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
    public int kthSmallest(TreeNode root, int k) {
        Queue<Integer> pq = new PriorityQueue<Integer>();
        
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode n = q.poll();
                pq.offer(n.val);
                if (n.left != null) {
                    q.offer(n.left);
                }                    
                if (n.right != null) {
                    q.offer(n.right);
                }
            }
        }
        
        int res = 0;
        for (int i = 0; i < k; i++) {
            res = pq.poll();
        }
        
        return res;
    }
}
