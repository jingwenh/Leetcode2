# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.maximum = -float('inf')
        self.traverse(root, 1)
        return self.maximum

    def traverse(self, root, cur_length):
        if cur_length > self.maximum:
            self.maximum = cur_length
        
        if root == None:
            return
        
        # 看子节点是不是递增的, 是递增的就递归下去
        if root.left != None and root.left.val == root.val + 1:
            self.traverse(root.left, cur_length + 1)

        if root.right != None and root.right.val == root.val + 1:
            self.traverse(root.right, cur_length + 1)
        
        self.traverse(root.left, 1)
        self.traverse(root.right, 1)
