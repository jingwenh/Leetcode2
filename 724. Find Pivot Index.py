# 把数组切成左半边和右半边
# 主要问题是不能重复计算左半边和右半边的和
class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        prv = 0
        left_sum = 0
        right_sum = sum(nums)
        for i, cur in enumerate(nums):
            left_sum = left_sum + prv
            right_sum = right_sum - cur
            print(left_sum, right_sum)
            if left_sum == right_sum:
                return i
            prv = cur
        
        return -1
