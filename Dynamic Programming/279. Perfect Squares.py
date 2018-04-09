class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 定义状态：dp[i]表示数字i最少由几个square number组成
        
        # 初始化
        dp = [float('inf') for _ in range(n + 1)] # 要算到n, 默认取inf因为后面要
        dp[0] = 0 # dp[4] = dp[4 - 4] + 1 = dp[0] + 1
        
        # 状态转移
        # 让i从1一直减到 j * j < i, 记录dp[i]可能的值，然后在其中取最小的
        for i in range(1, n + 1):
            j = 1
            possible_values = []
            while j * j <= i:
                val = dp[i - j * j] + 1
                possible_values.append(val)
                j = j + 1
            dp[i] = min(possible_values)
        
        # print(dp)
        return dp[-1]
        
        
        
        
