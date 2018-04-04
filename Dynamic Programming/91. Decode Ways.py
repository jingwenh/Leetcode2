# 划分型动态规划
# 到第i个字符为止的解密方式数量由前两位决定
# dp[i] = dp[i - 1] * 1{如果s[i - 1]可以解密} + dp[i - 2] * 1{如果s[i - 2]s[i - 1]可以解密} - 分成最后留两位还是一位两种情况
# 比如xxxxx123 - 两种划分方式 XXXXX12|3和XXXXX1|23
# 假设XXXXX12|3有100种解密方式（最后一个3解密成C），到XXXXX1|23有50种解密方式（最后23解密成W），两种情况加起来是150
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
            
        # 状态: dp[i]表示到第i个字符有几种解密方式
        
        # 初始化：
        dp = [0 for _ in range(len(s) + 1)] # 多建一位
        codes = [str(i) for i in range(1, 27)] # 必须是str，否则"01"转换成int会变成1
        
        dp[0] = 1 # 迷之定义，就必须是1，前0个字符的解密方式
        
        # 状态转移：dp[i] = dp[i - 1] * 1{如果s[i - 1]可以解密} + dp[i - 2] * 1{如果s[i - 2]s[i - 1]可以解密} - 分成最后留两位还是一位两种情况
        for i in range(1, len(s) + 1):
            dp[i] = 0
            if s[i - 1] in codes:
                dp[i] = dp[i - 1]
                print(dp[i])
            if i - 2 >= 0:
                if s[i - 2] + s[i - 1] in codes:
                    dp[i] = dp[i] + dp[i - 2]
                    print(dp[i])
        print(dp)
        
        # 出口
        return dp[-1]
        
