class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.m = m
        self.n = n
        
        # 状态定义：dp[i][j]表示从dp[0][0]到dp[i][j]的路径数量
        
        # 初始化：dp[0][0] = grid[0][0]
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1
        
        # 状态转移：到当前节点路径数量 = 从上往当前节点走路径数 + 从左...
        # dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        for i in range(m):
            for j in range(n):
                if (i, j) == (0, 0):
                    continue
                up = 0
                if self.inBound((i - 1, j)):
                    up = dp[i - 1][j]
                left = 0
                if self.inBound((i, j - 1)):
                    left = dp[i][j - 1]
                dp[i][j] = left + up
            
        # print(dp)
        
        # 终点：右下角
        return dp[-1][-1]
        
    def inBound(self, coo):
        if coo[0] >= 0 and coo[0] < self.m and coo[1] >= 0 and coo[1] < self.n:
            return True
        return False
