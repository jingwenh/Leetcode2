# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.levels = []
        self.helper(root)
        return [sum(l) / len(l) for l in self.levels]
    
    def helper(self, root):
        q = deque()
        q.append(root)
        while len(q) > 0:
            size = len(q)
            level = []
            for i in range(len(q)):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left != None:
                    q.append(cur.left)
                if cur.right != None:
                    q.append(cur.right)
            self.levels.append(level)
            
