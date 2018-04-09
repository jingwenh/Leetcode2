class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def isSquare(x):
            return x ** 0.5 == int(x ** 0.5)
        
        j = 0
        while c - j ** 2 >= 0:
            if isSquare(c - j * j):
                return True
            j = j + 1
        return False
    
