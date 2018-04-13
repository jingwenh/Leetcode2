class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # https://www.youtube.com/watch?v=rT5QSF4zcb8
        cur = 0
        res = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                cur = cur + 1 # 下一个数目和上一个数目的差
                res = res + cur
            else:
                cur = 0 # 否则差从0重新开始
        return res
