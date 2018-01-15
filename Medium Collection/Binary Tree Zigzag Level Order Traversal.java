/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
//层序遍历
//把奇数Index的列表reverse
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        
        if (root == null) {
            return res;
        }
        
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        
        while (!q.isEmpty()) {
            int size = q.size();
            List<Integer> list = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode n = q.poll();
                list.add(n.val);
                if (n.left != null) {
                    q.offer(n.left);
                }                    
                if (n.right != null) {
                    q.offer(n.right);
                }
            }
            res.add(list);
        }
        
        for (int i = 0; i < res.size(); i++) {
            if (i % 2 == 1) {
                reverseList(res.get(i));
            }
        }
        
        return res;
    }
    
    private void reverseList(List<Integer> list) {
        System.out.println(list);
        int cur1 = 0;
        int cur2 = list.size() - 1;
        while (cur1 <= cur2) {
            int temp = list.get(cur1);
            list.set(cur1, list.get(cur2));
            list.set(cur2, temp);
            cur1++;
            cur2--;
        }
        System.out.println(list);
    }
}
