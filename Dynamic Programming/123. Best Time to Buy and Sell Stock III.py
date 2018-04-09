class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        
        # 五个阶段：
        # 一次没买，买一次，买卖一次，买卖买，买卖买卖
        # 状态：第i天的手上的钱，处于j阶段
        
        # 初始化
        dp = [[0 for _ in range(5)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = -float('inf')
        dp[0][3] = -float('inf')
        dp[0][4] = -float('inf')
        
        
        # 状态转移：分阶段讨论，计算dp[i][0] ~ dp[i][4]
        # 状态n只能从状态n - 1转换而来，比如状态"买一次"只能从状态一次没买转换过来
        # 因此dp[i][j]的值只能在dp[i - 1][j](保持上一阶段状态)或在dp[i - 1][j - 1]之间取
        for i in range(1, len(prices)):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
            dp[i][2] = max(dp[i - 1][1] + prices[i], dp[i - 1][2])
            dp[i][3] = max(dp[i - 1][2] - prices[i], dp[i - 1][3])
            dp[i][4] = max(dp[i - 1][3] + prices[i], dp[i - 1][4])
        
        # print(dp)
        return max(dp[-1][0], dp[-1][2], dp[-1][4]) # 最后一次必须是没有持仓的状态，在0 2 4里面取
        
