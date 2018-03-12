# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        
        q = []
        q.append(root)
        res = []
        
        while len(q) > 0:
            # print(q)
            size = len(q)
            level = []
            for _ in range(size):
                cur = q.pop(0)
                level.append(cur.val)
                if cur.left != None:
                    q.append(cur.left)
                if cur.right != None:
                    q.append(cur.right)
            res.append(max(level))
        
        return res
