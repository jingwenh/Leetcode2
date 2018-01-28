public class Solution {
    /*
     * @param head: The head of linked list.
     * @return: You should return the head of the sorted linked list, using constant space complexity.
     */
     //用Merge sort
     //1. 切两半
     //2. 左边放进mergeSort递归
     //3. 右边放进mergeSort递归
     //4. 两边merge
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode mid = findMiddle(head);

        ListNode right = sortList(mid.next);
        mid.next = null; //清空右半边，把链表只剩左半边
        ListNode left = sortList(head);

        return merge(left, right);
    }
    
    //用来切链表
    private ListNode findMiddle(ListNode head) {
        ListNode slow = head, fast = head.next;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow;
    }
    
    //Merge两个链表
    private ListNode merge(ListNode head1, ListNode head2) {
        ListNode dummy = new ListNode(0);
        ListNode cur1 = head1;
        ListNode cur2 = head2;
        ListNode dummyCur = dummy;
        
        while (cur1 != null && cur2 != null) {
            if (cur1.val < cur2.val) {
                dummyCur.next = new ListNode(cur1.val); //可以写dummyCur.next = cur1;
                cur1 = cur1.next;
                dummyCur = dummyCur.next;
            } else {
                dummyCur.next = new ListNode(cur2.val); //可以写dummyCur.next = cur2;
                cur2 = cur2.next;
                dummyCur = dummyCur.next;
            }
        }
        
        if (cur1 == null) {
            dummyCur.next = cur2;
        }
        
        if (cur2 == null) {
            dummyCur.next = cur1;
        }
        
        return dummy.next;
    }
}
