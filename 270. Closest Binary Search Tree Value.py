# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        l = self.inorderTraverse(root)
        left = 0
        right = 1
        
        tpl_list = []
        for n in l:
            tpl_list.append((n, abs(n - target)))
        res = heapq.nsmallest(1, tpl_list, key = lambda tpl : tpl[1])
        return res[0][0]
    
    def inorderTraverse(self, root):
        res = []
        if root == None:
            return res
        
        res.extend(self.inorderTraverse(root.left))
        res.append(root.val)
        res.extend(self.inorderTraverse(root.right))
        
        return res
