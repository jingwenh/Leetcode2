# 设移动前数组和为sum, 数组最小值为min, 需要移动m次将最小值变成x， 一共有n个数
#  sum + m * (n - 1) = x * n (移动m次，每次将n-1个数++)
# 又有x = min + m (最小值每次都要参与移动)
# 得sum - min * n = m
class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)
        
