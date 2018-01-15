/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
//两根指针同时分别遍历两个链表
//resNode.val = carry + cur1.val + cur2.val;
//写法类似于merge two sorted lists
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode cur1 = l1;
        ListNode cur2 = l2;
        ListNode dummy = new ListNode(0);
        ListNode dummyCur = dummy;
        
        int carry = 0;
        while (cur1 != null && cur2 != null) {
            int sum = cur1.val + cur2.val + carry;
            if (sum >= 10) {
                sum = sum - 10;
                carry = 1;
            } else {
                carry = 0;
            }
            dummyCur.next = new ListNode(sum);
            dummyCur = dummyCur.next;
            cur1 = cur1.next;
            cur2 = cur2.next;
        }
        
        while (cur1 != null) {
            int sum = cur1.val + carry;
            if (sum >= 10) {
                sum = sum - 10;
                carry = 1;
            } else {
                carry = 0;
            }
            dummyCur.next = new ListNode(sum);
            dummyCur = dummyCur.next;
            cur1 = cur1.next;
        }
        
        while (cur2 != null) {
            int sum = cur2.val + carry;
            if (sum >= 10) {
                sum = sum - 10;
                carry = 1;
            } else {
                carry = 0;
            }
            dummyCur.next = new ListNode(sum);
            dummyCur = dummyCur.next;
            cur2 = cur2.next;            
        }
        
        if (carry == 1) {
            dummyCur.next = new ListNode(1);
        }
        
        return dummy.next;
    }
}
