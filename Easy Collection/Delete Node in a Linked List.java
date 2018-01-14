/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
//因为没有之前的节点，不能真正意义上的删除
//把后面的链表复制的值到前面去（shift by 1 step to the front）
class Solution {
    public void deleteNode(ListNode node) {
        // -> 3 -> 4 -> 5 -> 6，假设要删掉3
        // -> 4 -> 4 -> 5 -> 6，先把后面的4复制到3
        // -> 4 -> 5 -> 6，再把第二个4后面的链表接到原来3的后面（删掉第二个4）
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
