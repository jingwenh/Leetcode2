class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        
        # 定义状态: dp[i][j]是以matrix[i][j]为右下角的最大正方形边长
        
        # 初始化:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        if matrix[0][0] == 1:
            dp[0][0] = 1
        
        # 状态转移
        # https://leetcode.com/problems/maximal-square/solution/
        # 上、左、左上三块中，取最小的边长+1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        
        res = -float('inf')
        for l in dp:
            maximum = max(l)
            if maximum > res:
                res = maximum
        
        # print(dp)
        
        # 最后返回的是面积
        return res ** 2
