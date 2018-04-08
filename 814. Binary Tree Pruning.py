# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        
        self.flag = False
        
        while True:
            self.removeZero(root, None, None)
            if self.flag == True:
                self.flag = False
            else:
                break
        return root
    
    def removeZero(self, root, prv, leftOrRight):
        if root == None:
            return
        
        if root.left == None and root.right == None and root.val == 0:
            self.flag = True
            if leftOrRight == "left":
                prv.left = None
            else:
                prv.right = None
        
        self.removeZero(root.left, root, "left")
        self.removeZero(root.right, root, "right")
        
