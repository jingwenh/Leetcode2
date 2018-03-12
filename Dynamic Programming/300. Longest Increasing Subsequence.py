# Pure DP, TLE
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        # 子序列 vs. 子数组：子序列可以不是连续的
        # 状态定义：dp[i]表示到i的最长子序列
        
        # 初始化
        dp = [[] for i in range(len(nums))]
        dp[0] = list(nums[0:1])
        
        # 状态转移：
        # 到前面去找哪个位置的数字比当前这个数字nums[i]要小，到位置i的序列 = 找到的序列中最长的 + nums[i]
        for i in range(1, len(nums)):
            longest_prv_seq = []
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if len(dp[j]) > len(longest_prv_seq):
                        longest_prv_seq = list(dp[j])
            dp[i] = list(longest_prv_seq)
            dp[i].append(nums[i])
        
        # 终点：dp里最长的
        res = []
        for seq in dp:
            if len(seq) > len(res):
                res = seq
        return len(res)
