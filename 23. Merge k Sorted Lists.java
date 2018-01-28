/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>(7, new ListComparator());
        for (ListNode l : lists) {
            if (l != null) {
                pq.offer(l);
            }
        }
        ListNode dummy = new ListNode(0);
        ListNode dCur = dummy;
        while (!pq.isEmpty()) {
            ListNode min = pq.poll();
            dCur.next = new ListNode(min.val);
            dCur = dCur.next;
            if (min.next != null) {
                pq.offer(min.next);
            }
        }
        return dummy.next;
    }
    
    private class ListComparator implements Comparator<ListNode> {
        public int compare(ListNode l1, ListNode l2) {
            return l1.val - l2.val;
        }
    }
    
    
}
