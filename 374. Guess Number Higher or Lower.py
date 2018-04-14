# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while left + 1 < right:
            mid = int((left + right) / 2)
            g = guess(mid)
            if g == 1:
                left = mid
            if g == -1:
                right = mid
            if g == 0:
                return mid
        
        if guess(left) == 0:
            return left
        if guess(right) == 0:
            return right
                
