# Solution 1: Pure BFS, Time limit exceeded
# 找出所有path，然后选出path sum最小的
# 时间复杂度分析：每走到一个节点都要两个分叉，如果高度为n，时间复杂度为O(2^n)
from collections import deque
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        q = deque()
        q.append([(0, 0)])
        res = []
        self.triangle = triangle
        while len(q) > 0:
            cur = q.popleft()
            if len(cur) == len(triangle):
                path_sum = 0
                for c in cur:
                    path_sum = path_sum + triangle[c[0]][c[1]]
                res.append(path_sum)
            c = cur[-1]
            next_pos1 = (c[0] + 1, c[1])
            next_pos2 = (c[0] + 1, c[1] + 1)
            if self.inBound(next_pos1):
                next_path = list(cur)
                next_path.append(next_pos1)
                q.append(next_path)
            if self.inBound(next_pos2):
                next_path = list(cur)
                next_path.append(next_pos2)
                q.append(next_path)
        return min(res)
                
    def inBound(self, coo):
        width = coo[0]
        if coo[0] > 0 and coo[0] < len(self.triangle) and coo[1] >= 0 and coo[1] <= width:
            return True
        return False

# Solution 2: traverse as a binary tree, TLE
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.min_path = float('inf')
        self.triangle = triangle
        self.traverse((0, 0), 0)
        return self.min_path
        
    def traverse(self, root, path_sum):
        path_sum = path_sum + self.triangle[root[0]][root[1]]
        if root[0] == len(self.triangle) - 1:
            self.min_path = min(self.min_path, path_sum)
            return
        self.traverse((root[0] + 1, root[1]), path_sum)
        self.traverse((root[0] + 1, root[1] + 1), path_sum)

# Solution 3: divide and conquer, TLE
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.triangle = triangle
        min_path = self.divideConquer((0, 0))
        return min_path
        
    # 最短路径 = min(左边最短，右边最短)
    def divideConquer(self, root):
        if root[0] == len(self.triangle) - 1:
            return self.triangle[root[0]][root[1]]
        
        left_min_sum = self.divideConquer((root[0] + 1, root[1]))
        right_min_sum = self.divideConquer((root[0] + 1, root[1] + 1))
        return self.triangle[root[0]][root[1]] + min(left_min_sum, right_min_sum)
