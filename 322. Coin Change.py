class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # edge cases: 剔除掉不能用的硬币，amount = 0返回0
        if amount == 0:
            return 0
        
        for c in coins:
            if c > amount:
                coins.remove(c)
        if len(coins) == 0:
            return -1
        
        # 定义状态：dp[i]表示i元钱最少要多少个硬币拼好
        
        # 初始化：0元要0个硬币，其它都是无穷大（0元设0保证dp(c) = 1, 其它无穷大保证求min时不影响结果）
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        
        # 转移方程：dp[i] = min(dp[i - c]) + 1, 如果求出inf就是拼不出这个面额
        for i in range(1, amount + 1):
            # if i in coins:
            #     continue
            prv = []
            for c in coins:
                prv.append(i - c)
            options = []
            for num in prv:
                if num <= amount and num >= 0:
                    options.append(dp[num])
                else: # 这里要处理越界，比如amount = 3, coin = 5，此时会越界
                    options.append(float('inf'))
            
            dp[i] = min(options) + 1
        
        # 终点：dp[amount]
        return dp[-1] if dp[-1] != float('inf') else -1
                
        
