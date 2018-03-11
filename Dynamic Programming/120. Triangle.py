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
    
# Solution 5: DP with iteration
# Recursion vs. Iteration:
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        # 定义状态： f[i][j]表示从底端到节点(i, j)的最短路径
        f = [[float('inf') for i in range(len(triangle[-1]))] for j in range(len(triangle))]
        
        # 初始化最底端
        for i in range(len(f[-1])):
            f[-1][i] = triangle[-1][i]
        
        # 循环自底向上求解(从倒数第二行开始)，每个节点的min_path = min(左min_path, 右min_path) + 这个节点的值
        for i in range(len(triangle) - 2, -1, -1): # range(起始值，步长，exclusive结束值)
            for j in range(len(triangle[i])): # 列按正常顺序遍历
                f[i][j] = min(f[i + 1][j], f[i + 1][j + 1]) + triangle[i][j]
        
        return f[0][0]
 
# Solution 6: DP iteration with Top-down approach
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 自顶向下求解
        # 定义状态： f[i][j]表示从(0, 0)到(i, j)的最短路径
        f = [[float('inf') for i in range(len(triangle[-1]))] for j in range(len(triangle))]
        
        # 初始化f[0][0]
        f[0][0] = triangle[0][0]
        
        # 循环自顶向下求解f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
        # 根据递推公式，最左边和最右边会越界，最左边、最右边、中间部分分开处理
        for i in range(1, len(triangle)): # 从第二层开始
            f[i][0] = f[i - 1][0] + triangle[i][0]
            f[i][i] = f[i - 1][i - 1] + triangle[i][i] #注意f的形状和triangle不一样, 不要用-1求f最末尾的值
        
        # 从第二层开始
        for i in range(1, len(triangle)):
            for j in range(1, i):
                f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
        
        # 取最后一层的最小值
        return min(f[-1])
