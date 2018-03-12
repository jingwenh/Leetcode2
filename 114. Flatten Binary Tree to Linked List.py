# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return: 
    """
    def flatten(self, root):
        # write your code here
        if root == None:
            return None
        
        root, rl = self.helper(root)
    
    # 分四种情况分别递归flatten
    def helper(self, root):
        if root.left == None and root.right == None:
            return (root, root)
        
        if root.left != None and root.right != None:
            left, left_rl = self.helper(root.left)
            right, right_rl = self.helper(root.right)
            
            root.left = None
            root.right = None
            
            root.right = left
            left_rl.right = right
            
            return (root, right_rl)
        
        if root.right != None:
            right, right_rl = self.helper(root.right)
            return (root, right_rl)
        
        if root.left != None:
            left, left_rl = self.helper(root.left)
            root.left = None
            root.right = left
            return (root, left_rl)
