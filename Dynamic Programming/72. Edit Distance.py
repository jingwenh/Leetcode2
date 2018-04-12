class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == word2:
            return 0
        
        # 定义状态：dp[i][j]表示使得word1[0:i] == word2[0:j]需要几步
        
        # 初始化：
        dp = [[float('inf') for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        dp[0][0] = 0
        
        # 状态转移：求出所有的dp
        # 分情况讨论
        # 1. 如果word1[0:i] == word2[0:j]: dp[i][j] = dp[i-1][j-1]
        # 2. 如果不相等：
        # 2.1 Insertion: 比如word1[0:i] = a, word2[0:j] = ae, word1[0:i] + word2[j-1] = new_word1[0:i] -> dp[i][j] = dp[i][j-1] + 1 
        # (从word2[0:j-1]添加一个字母到word2[0:j]，使得word1[0:i] == word2[0:j])
        # 2.2 Delete: word1[0:i] = ae, word2[0:j] = a, word1[0:i] - word1[i-1] = word2[0:j] -> dp[i][j] = dp[i-1][j] + 1
        # (从word1[0:i-1]添加一个字母到word1[0:i]，使得word1[0:i] == word2[0:j])
        # 2.3 replace: dp[i][j] = dp[i-1][j-1] + 1
        # (把不同的那一个字母看作多余的字母，即word1[0:i]和word2[0:j]各多一个字母，即从word1[0:i-1]和word2[0:j-1]同时添加一个字母)
        
        # 综合考虑：
        # dp[i][0] = i
        # dp[0][j] = j
        # dp[i][j] = dp[i - 1][j - 1], if word1[i - 1] == word2[j - 1]
        # dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1), if word1[i - 1] != word2[j - 1]
        
        for i in range(len(word1) + 1):
            dp[i][0] = i # 从word1[0:i]到word2[0:0]要i步，即删掉i个字符
        for j in range(len(word2) + 1):
            dp[0][j] = j # 从word1[0:0]到word2[0:j]要j步，即添加j个字符
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                else: # 三个操作取最小
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        
        # print(dp)
        
        return dp[-1][-1]
