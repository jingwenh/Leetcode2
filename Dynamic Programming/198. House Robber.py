class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        # 状态：dp[i][0]表示第i间房子不抢，到当前最大的钱数；dp[i][1]表示第i间房子抢，到当前最大的钱数
        
        # 初始化：
        dp = [[0, 0] for i in range(len(nums))]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        
        # 状态转移
        # 如果上一间房子被抢了：dp[i][0] = dp[i - 1][1]; dp[i][1] = -float('inf') 如果抢了就报警了
        # 如果上一间房子没被抢：dp[i][0] = dp[i - 1][0]; dp[i][1] = dp[i - 1][0] + nums[i]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
            # dp[i][1] = max(dp[i - 1][0] + nums[i], -float('inf'))
            dp[i][1] = dp[i - 1][0] + nums[i]
        
        return max(dp[-1])
        
