class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or k < 1:
            return 0

        # III的follow up
        # 2k + 1个阶段：
        # 如果状态码是偶数，则属于没有持仓的状态
        # 如果状态码是奇数，则属于有持仓的状态
        # 状态：第i天的手上的钱，处于j阶段
        
        # 初始化
        dp = [[-float('inf') for _ in range(2 * k + 1)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        # print(dp)
        # 状态转移：分阶段讨论
        # 状态n只能从状态n - 1转换而来，比如状态"买一次"只能从状态一次没买转换过来
        # 因此dp[i][j]的值只能在dp[i - 1][j](保持上一阶段状态)或在dp[i - 1][j - 1]之间取
        # 从持仓状态到非持仓状态，+prices[i] (奇数到偶数)
        # 从非持仓状态到持仓状态，-prices[i] (偶数到奇数)
        for i in range(1, len(prices)):
            dp[i][0] = dp[i - 1][0]
            for j, state in enumerate(dp[i]):
                if j == 0:
                    continue
                if j % 2 == 0:
                    dp[i][j] = max(dp[i - 1][j - 1] + prices[i], dp[i - 1][j]) # 当前状态偶数，上一个状态是奇数
                else:
                    dp[i][j] = max(dp[i - 1][j - 1] - prices[i], dp[i - 1][j]) # 当前状态奇数，上一个状态是偶数
            
        
        # print(dp)
        res = []
        for j, state in enumerate(dp[-1]):
            if j % 2 == 0:
                res.append(state)
            
        return max(res) # 最后一次必须是没有持仓的状态
