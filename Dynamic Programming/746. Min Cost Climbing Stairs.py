class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 定义状态：dp[i]表示到第i层台阶的最小cost
        
        # 初始化：从第一个台阶开始或者从第二个台阶开始，算的是走出台阶的cost，为了方便把终点也加进去
        cost.append(0)
        dp = [float('inf') for i in range(len(cost))]
        dp[0] = 0
        dp[1] = 0
        
        # 注意往前走才收费，到这个台阶不收费
        # 状态转移：到第i层台阶的min_cost = min(从i - 1到i的cost, 从i - 2到i的cost)
        for i in range(2, len(cost)):
            # 不用管i = 1时dp[i - 2]越界，dp[-1] = inf
            c1 = dp[i - 1] + cost[i - 1]
            c2 = dp[i - 2] + cost[i - 2]
            dp[i] = min(c1, c2)
        
        # 终点，算走出所有台阶的cost
        return dp[-1]
