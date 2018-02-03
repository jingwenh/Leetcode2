/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
//类似于Clone graph
//先复制节点
//用一个HashMap映射老节点和新节点
//根据老节点的连接关系连接新节点
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        HashMap<RandomListNode, RandomListNode> map = new HashMap<>();
        RandomListNode cur = head;
        //Copy
        while (cur != null) {
            RandomListNode newNode = new RandomListNode(cur.label);
            map.put(cur, newNode);
            cur = cur.next;
        }
        //Connect
        for (RandomListNode key : map.keySet()) {
            RandomListNode newNode = map.get(key);
            RandomListNode nextNode = map.get(key.next);
            RandomListNode randomNode = map.get(key.random);
            newNode.next = nextNode;
            newNode.random = randomNode;
        }
        
        return map.get(head);
    }
}
