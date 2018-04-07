class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        
        # 定义状态：dp[i]表示到第i个数字，最大的长度
        
        # 初始化：
        dp = [0 for _ in range(len(nums))]
        dp[0] = 1
        
        # 转移方程：两种情况
        # 到第i个数字开始递减，1 2 3 4 2，最后一位数为第i位，dp[i] = 1
        # 第i个数仍递增，1 2 3 4 5，dp[i] = dp[i - 1] + 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1
        
        print(dp)
        
        # 出口：返回dp里最大的
        return max(dp)

# Follow up: 既可以从左也可以从右开始 - 反着来再dp一次
