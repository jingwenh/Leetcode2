class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # dp[i]表示数字i的二进制有几个1
        
        # 初始化：
        dp = [0 for _ in range(num + 1)]
        
        # 状态转移：dp(x) = dp(x & (x−1)) + 1;
        for i in range(1, num + 1):
            dp[i] = dp[i & (i - 1)] + 1
        
        # 出口：返回整个dp
        return dp
