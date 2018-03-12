class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 状态定义：dp[i]表示到第i层台阶有几种走法, 0-indexing
        
        # 初始化：
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        
        # 状态转移：到第i层台阶走法数量 = 到第(i - 1)层台阶走法数量 + 到第(i - 2)层台阶走法数量
        # dp[i] = dp[i - 1] + dp[i - 2]
        for i in range(1, n + 1):
            s1 = 0
            if i - 1 >= 0:
                s1 = dp[i - 1]
            s2 = 0
            if i - 2 >= 0:
                s2 = dp[i - 2]
            dp[i] = s1 + s2
        
        # 终点：第n个台阶
        return dp[-1]
        
