# TLE
# 划分型动态规划，枚举前面所有符合要求的状态（可以作为上一步状态的状态），取其中最大或最小用于下一步递推
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 定义状态：dp[i]表示前i个字符(s[0:i])能划分成几个回文串
        # 初始化：
        dp = [0 for _ in range(len(s) + 1)] # 要取到dp[len(s)]， dp长度要定义为len(s) + 1
        
        # 状态转移:
        # 从第i个字符向前找，直到s[j:i]能组成最长的一个回文串，此时dp[i] = dp[j] + 1
        # 比如aabcbd，从i = 5向前找，找到最长的回文串为s[2:5] = bcb, 则dp[5] = dp[2] + 1
        # 再比如aadcbd，从i = 5向前找，找到最长的回文串为s[4:5] = b, 则dp[5] = dp[4] + 1
        for i in range(1, len(s) + 1):
            prv = s[:i]
            dps = []
            # 枚举所有符合要求的上一个状态
            # 往前找，记录可以组成回文串的起点，最后取最小的dp[j]
            for j in range(i):
                if self.isPal(s[j:i]):
                    dps.append(dp[j])
            dp[i] = min(dps) + 1
        
        print(dp)
        return dp[-1] - 1
    
    def isPal(self, s):
        # print(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left = left + 1
            right = right - 1
        return True

# 优化解法：缓存每一位结尾的回文串最大长度
