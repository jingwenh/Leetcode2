/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
//先分别计算两个链表的长度
//然后用创建两个指针
//其中一个指针先在较长的那个链表上移动，移动多出的长度（保证两个指针可以相遇）
//然后两个指针同时往后移，直到两个指针相遇，相遇的节点为intersect
//比如在题目给出的例子里，创建cur1和cur2，让cur2先移到b2的位置，然后两个指针同时往后移
//两个指针就会在c1相遇
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int l1 = 1;
        ListNode cur1 = headA;
        while (cur1 != null && cur1.next != null) {
            l1 = l1 + 1;
            cur1 = cur1.next;
        }
        int l2 = 1;
        ListNode cur2 = headB;
        while (cur2 != null && cur2.next != null) {
            l2 = l2 + 1;
            cur2 = cur2.next;
        }
        
        int diff = l1 - l2;
        
        if (diff > 0) { //A更长
            cur1 = headA;
            for (int i = 0; i < diff; i++) {
                cur1 = cur1.next;
            }
            cur2 = headB;
        } else { //B更长
            cur2 = headB;
            for (int i = 0; i < -diff; i++) {
                cur2 = cur2.next;
            }
            cur1 = headA;
        }
        
        while (cur1 != null && cur2 != null && cur1 != cur2) {
            cur1 = cur1.next;
            cur2 = cur2.next;
        }
        
        if (cur1 == cur2) {
            return cur1;
        } else {
            return null;
        }
    }
}
