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

# Solution 2: DFS, traverse as a binary tree, TLE
# Unable to optimize
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
# 优化：缓存每个节点的min path sum
# TLE的原因：重复走节点，并且对于相同的节点，从底端到它的min path sum是不变的
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

# Solution 4: divide and conquer + 缓存节点的path sum, AC
# DP vs. Divide and Conquer: 子问题有没有重叠
# 此时时间复杂度是O(n^2)
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.cache_min_path_sum = {}
        self.triangle = triangle
        min_path = self.divideConquer((0, 0))
        return min_path
        
    # 最短路径 = min(左边最短，右边最短)
    def divideConquer(self, root):
        if root[0] == len(self.triangle) - 1:
            return self.triangle[root[0]][root[1]]
        
        # 缓存过了这个节点的path sum ，直接返回
        if root in self.cache_min_path_sum.keys():
            return self.cache_min_path_sum[root]
        
        left_min_sum = self.divideConquer((root[0] + 1, root[1]))
        right_min_sum = self.divideConquer((root[0] + 1, root[1] + 1))
        min_path_sum_to_cur = self.triangle[root[0]][root[1]] + min(left_min_sum, right_min_sum)
        
        # 加缓存
        self.cache_min_path_sum[root] = min_path_sum_to_cur
        
        return self.triangle[root[0]][root[1]] + min(left_min_sum, right_min_sum)
