# 注意索引：
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 定义状态：dp[i]表示到第i个字母为止，从上一个找到单词的字符的下一个字符开始，能不能组成一个单词
        
        # 初始化：
        dp = [False for i in range(len(s) + 1)] # 第一位是占位符
        dp[0] = True
        
        # 状态转移：一个指针j从0移到i, 当dp[j]=True时, 判断s[j:i+1]是不是构成一个单词，如果构成单词，把dp[i + 1]设成True
        # 注意索引：
        #     0 1 2 3 4 5 6 7 8
        # dp: T F F F T F F F T
        #     . l e e t c o d e
        #       0 1 2 3 4 5 6 7
        for i in range(0, len(s)): # 从0开始不是从1开始，因为初始化时标记的是占位符的状态，不是第一个字符的状态
            for j in range(0, i + 1):
                if dp[j] == True and s[j:i+1] in wordDict:
                    dp[i + 1] = True
        # print(dp)
        # 终点：
        return dp[-1]
