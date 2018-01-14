/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        //1 -> 2 -> 3 -> null
        
        ListNode cur = head;
        ListNode prv = null;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = prv;
            prv = cur;
            cur = next;
        }
        
        return prv;
    }
}
