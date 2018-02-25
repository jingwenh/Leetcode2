# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 把每个node都放进list
# 然后reverse这个list
# 然后按顺序拼接链表和字符串
class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        forward = []
        cur = head
        while cur != None:
            forward.append(cur)
            cur = cur.next
        backward = list(reversed(forward))
        
        # 解开所有的链接
        for n in forward:
            n.next = None
        
        dummy = ListNode(0)
        prv = dummy
        for i in range(len(forward)):
            prv.next = forward[i]
            if forward[i] != backward[i]: # 两个节点不相等，直接拼接
                forward[i].next = backward[i]
            else:
                break
            if backward[i] == forward[i + 1]: # 到下一个节点开始就循环回去了，直接结束
                break
            prv = backward[i]
        
        
