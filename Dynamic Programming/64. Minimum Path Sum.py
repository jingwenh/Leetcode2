class Solution:
    def minPathSum(self, grid):
        self.grid = grid
        
        # 状态：dp[i][j]表示从dp[0][0]到dp[i][j]的最短距离
        
        # 初始化：dp[0][0] = grid[0][0]
        dp = [[float('inf') for i in range(len(grid[0]))] for j in range(len(grid))]
        dp[0][0] = grid[0][0]
        
        
        # 状态转移：到当前节点的最短路径在左、上方取（只能向右下走）
        # dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) == (0, 0): # 一定要记得跳过处理过的点！！！
                    continue
                up = float('inf')
                if self.inBound((i - 1, j)):
                    up = dp[i - 1][j]
                left = float('inf')
                if self.inBound((i, j - 1)):
                    left = dp[i][j - 1]
                dp[i][j] = min(left, up) + grid[i][j]
        
        # 终点：右下角节点
        return dp[-1][-1]
    
    def inBound(self, coo):
        if coo[0] >= 0 and coo[0] < len(self.grid) and coo[1] >= 0 and coo[1] < len(self.grid[0]):
            return True
        return False
            
            
             
