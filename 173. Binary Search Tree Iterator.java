/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
//PriorityQueue
public class BSTIterator {

    PriorityQueue<TreeNode> pq;
    
    public BSTIterator(TreeNode root) {
        pq = new PriorityQueue<TreeNode>(7, new TreeNodeComparator());
        helper(root, pq);
    }
    
    private void helper(TreeNode root, PriorityQueue<TreeNode> pq) {
        if (root == null) {
            return;
        }
        pq.add(root);
        helper(root.left, pq);
        helper(root.right, pq);
    }
    
    private class TreeNodeComparator implements Comparator<TreeNode> {
        public int compare(TreeNode t1, TreeNode t2) {
            return (t1.val - t2.val);
        }
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !pq.isEmpty();
    }

    /** @return the next smallest number */
    public int next() {
        return pq.poll().val;
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */
