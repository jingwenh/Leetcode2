class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0
        
        # 定义状态：0-indexed
        # dp[i][j]表示前i栋房子，且第i栋是颜色j的最小花费
        
        # 初始化：
        dp = [[0 for i in range(len(costs[0]))] for j in range(len(costs))]
        for j in range(len(costs[0])):
            dp[0][j] = costs[0][j]
        
        
        # 状态转移：
        # dp[i][j] = min(dp[i - 1][indexes without j]) + costs[i][j]  如果现在这要要涂j，前面不能有j
        for i in range(1, len(costs)):
            for j in range(len(costs[0])):
                prv_costs = list(dp[i - 1])
                del prv_costs[j]
                dp[i][j] = min(prv_costs) + costs[i][j]
                
        return min(dp[-1])
