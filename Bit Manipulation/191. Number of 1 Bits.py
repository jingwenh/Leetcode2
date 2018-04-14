# 不断&1判断最后一位是不是1，然后右移
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for _ in range(32):
            if n & 1 == 1:
                count = count + 1
            n = n >> 1
        return count
