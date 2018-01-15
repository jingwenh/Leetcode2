/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
//层序遍历把节点按层放进list
//然后把每层的节点连起来
public class Solution {
    public void connect(TreeLinkNode root) {
        if (root == null) {
            return;
        }
        
        Queue<TreeLinkNode> q = new LinkedList<>();
        q.offer(root);
        List<List<TreeLinkNode>> tree = new ArrayList<>();
        
        while (!q.isEmpty()) {
            int size = q.size();
            List<TreeLinkNode> list = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeLinkNode n = q.poll();
                list.add(n);
                if (n.left != null) {
                    q.offer(n.left);
                }
                if (n.right != null) {
                    q.offer(n.right);
                }
            }
            tree.add(list);
        }
        
        for (List<TreeLinkNode> level : tree) {
            for (int i = 0; i < level.size(); i++) {
                TreeLinkNode n = level.get(i);
                if (i < level.size() - 1) {
                    n.next = level.get(i + 1);                    
                } else {
                    n.next = null;
                }

            }
        }
        
    }
}
