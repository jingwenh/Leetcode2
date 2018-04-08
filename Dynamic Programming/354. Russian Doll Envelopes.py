# TLE
class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if len(envelopes) == 0:
            return 0
        
        # 先把所有信封按长度排序
        # 如果信封Ej能套进Ei，那么在排序后的数组中一定有j > i
        # 状态定义：dp[i]表示第i个信封能套进信封的最大数量（包括自己）
        
        # 初始化：
        envelopes = heapq.nsmallest(len(envelopes), envelopes, key = lambda l : l[0])
        dp = [1 for _ in range(len(envelopes))]
        
        # print(envelopes)
        
        # 状态转移：
        # 向前遍历，如果envelopes[j]的宽度 > envelopes[i]的宽度，envelopes[j]的长度 > envelopes[i]的长度，dp[j] = dp[j] + 1，在所有结果里取最大
        for i in range(1, len(envelopes)):
            nums = []
            for j, e in enumerate(envelopes[:i]):
                if envelopes[i][1] > e[1] and envelopes[i][0] > e[0]:
                    nums.append(dp[j] + 1)
            if len(nums) != 0:
                dp[i] = max(nums)
        
        # print(dp)
        
        return max(dp)
