class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        
        for p in (2, 3, 5):
            # 按顺序除以2 3 5，不停地除以一个数，直到除不尽为止
            while num % p == 0:
                num /= p
        return num == 1
