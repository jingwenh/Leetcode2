# Solution 1: Pure BFS, Time limit exceeded
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
