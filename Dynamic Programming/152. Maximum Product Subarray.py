class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 定义状态：dp[i]是元组，表示在位置i的最大乘积和最小乘积(min, max)
        
        # 初始化：
        dp = [(-float('inf'), float('inf')) for n in nums]
        dp[0] = (nums[0], nums[0])
        
        # 状态转移：
        # dp[i]的最大值在nums[i], nums[i] * dp[i - 1][0], nums[i] * dp[i - 1][1]里取
        # 最小值也是
        # 因为dp[i - 1]里的最大最小值是累积相乘连续的元素得到，所有后面的dp[i]也可以保证是累积相乘连续的元素得到
        for i in range(1, len(nums)):
            min_n = min(nums[i], nums[i] * dp[i - 1][0], nums[i] * dp[i - 1][1])
            max_n = max(nums[i], nums[i] * dp[i - 1][0], nums[i] * dp[i - 1][1])
            dp[i] = (min_n, max_n)
        
        # 终点：所有元组里面最大的数
        pq = []
        for t in dp:
            pq.append(t[0])
            pq.append(t[1])
        return heapq.nlargest(1, pq)[0]
