/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
//1. 把链表“切两半”：先计算长度，再用两个指针分别指向两个链表头
//2. 把右半边reverse
//3. 比较两个链表
class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null) {
            return true;
        }
        
        int length = 1;
        ListNode cur = head;
        while (cur.next != null) {
            cur = cur.next;
            length++;
        }
        
        ListNode head1 = head;
        
        int startIndex2 = length / 2;
        cur = head;
        int count = 0;
        while (cur != null) {
            if (count == startIndex2) {
                break;
            }
            cur = cur.next;
            count++;
        }
        ListNode head2 = cur;
        
        head2 = reverseList(head2);
        
        ListNode cur1 = head1;
        ListNode cur2 = head2;
        while (cur1 != null && cur2 != null) {
            if (cur1.val != cur2.val) {
                return false;
            }
            cur1 = cur1.next;
            cur2 = cur2.next;
        }
        
        return true;
    }
    
    
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
