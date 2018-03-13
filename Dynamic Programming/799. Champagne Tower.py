class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        # 状态：dp[i][j]表示第i,j个杯子里装了多少酒，要向两边溢出多少(hold, overflow)
        
        # 初始化：
        dp = [[(0, 0) for i in range(100)] for j in range(100)]
        if poured > 1:
            dp[0][0] = (1, (poured - 1) / 2)
        else:
            dp[0][0] = (poured, 0)
        
        # 状态转移：自顶向下，下层杯子倒入的量等于上层左右两边溢出的量, poured = dp[i-1][j-1] + dp[i-1][j] 
        for i in range(query_row + 1):
            for j in range(i + 1):
                if (i, j) == (0, 0):
                    continue
                poored = dp[i-1][j-1][1] + dp[i-1][j][1]
                if poored > 1:
                    overflow = poured - 1 / 2
                    dp[i][j] = (1, (poored - 1) / 2)
                else:
                    overflow = 0
                    dp[i][j] = (poored, overflow)
        
        # 终点：dp[query_row][query_glass][0]
        return dp[query_row][query_glass][0]
        
