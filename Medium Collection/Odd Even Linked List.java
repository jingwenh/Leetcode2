/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
//把偶数节点从原来的链表里拆出来
//再把两个链表拼在一起
//只要不是复制原链表的每个节点，空间复杂度就是O(1)
class Solution {
    public ListNode oddEvenList(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prv = dummy;
        ListNode cur = head;
        
        ListNode evenHead = new ListNode(0);
        ListNode evenCur = evenHead;
        int count = 1;
        while (cur != null) {
            if (count % 2 == 0) {
                //拆出节点
                prv.next = cur.next;
                evenCur.next = cur;
                cur = cur.next;
                
                //偶数链表末端要设成null
                evenCur = evenCur.next;
                evenCur.next = null;
            } else {
                prv = cur;
                cur = cur.next;
            }
            count++;
        }
        //print(dummy.next); 
        //print(evenHead.next); 
        
        
        cur = dummy;
        while (cur.next != null) {
            cur = cur.next;
        }
        cur.next = evenHead.next;
        return dummy.next;
    }
    
}
