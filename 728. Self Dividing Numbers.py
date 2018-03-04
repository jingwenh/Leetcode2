class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right + 1):
            num = str(i)
            flag = True
            for c in num:
                if int(c) == 0 or i % int(c) != 0:
                    flag = False
                    break
            if flag == True:
                res.append(i)
        return res
        
