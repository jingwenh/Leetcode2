/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
//要用一个dummy，因为可能要删除链表头
//1. 计算链表长度
//2. 计算倒数第n个节点是正数第几个节点（length - n + 1）
//3. 按顺序删掉第（length - n + 1）个节点
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int length = 1;
        ListNode cur = head;
        while (cur.next != null) {
            cur = cur.next;
            length++;
        }
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        int count = 1;
        int delete = length - n + 1;
        cur = head;
        ListNode prv = dummy;
        
        while (cur != null) {
            if (count == delete) {
                System.out.println("delete");
                prv.next = cur.next;
                break;
            }
            prv = cur;
            cur = cur.next;
            count++;
        }
        
        return dummy.next;
    }
}
