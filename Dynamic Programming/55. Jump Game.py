class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # nums[i]表示能从i往前跳的步数
        # 状态：dp[i]表示能从第i - 1个节点到达第i个节点
        
        # 初始化：
        dp = [False for i in range(len(nums))]
        dp[0] = True
        
        # 状态转移：能否到达第i个节点 = 遍历前面的节点，判断前面是否有任意一个节点能到第i个节点
        for i in range(1, len(nums)):
            for j in range(0, i):
                # 从位置j能走到的最远位置在i后面，并且位置j是可以走到的
                if j + nums[j] >= i and dp[j] == True:
                    dp[i] = True
                    break
        
        # print(dp)
        
        # 终点：最后一个节点的情况
        return dp[-1]
