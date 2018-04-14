# 利用XOR，两个相同的数XOR = 0
# 类似于使用set, 如果遇到了相同的数把数字移出set, 最后集合里剩下的数是single number
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            res = res ^ n
        return res
