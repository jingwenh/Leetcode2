class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0
        
        # 定义状态：0-indexed
        # dp[i][0]表示前i栋房子，且第i栋是颜色0的最小花费
        # dp[i][1]表示前i栋房子，且第i栋是颜色1的最小花费
        # dp[i][2]表示前i栋房子，且第i栋是颜色2的最小花费
        
        # 初始化：
        dp = [[0 for i in range(3)] for j in range(len(costs))]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        
        
        # 状态转移：
        # dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]  如果现在这要要涂0，前面只能涂1 2
        # dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
        # dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
        for i in range(1, len(costs)):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
        
        print(dp)
        return min(dp[-1][0], dp[-1][1], dp[-1][2])
        
        
