class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if k == 0 or n == 0:
            return 0
        
        # 注意是no more than 2，意思是可以两个相邻的颜色相同，但是不能3个相邻的颜色相同
        # 定义状态：dp[i][0]表示第i个post的涂法数量, 且颜色和前面不相同；dp[i][1]表示第i个post的涂法数量, 且颜色和前面相同
        
        # 初始化
        dp = [[0, 0] for i in range(n)]
        dp[0][0] = k
        dp[0][1] = 0
        
        # 转移方程:
        # dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) * (k - 1) 前面post的所有情况（不是取最大）* (k - 1)
        # dp[i][1] = dp[i - 1][0] 前面的post和再前面一个不能是相同颜色
        for i in range(1, n):
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) * (k - 1)
            dp[i][1] = dp[i - 1][0]
        
        # 终点
        return sum(dp[-1])
    
