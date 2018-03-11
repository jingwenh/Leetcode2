class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        max_shifts = len(A)
        for i in range(max_shifts):
            A = A[1:] + A[0]
            if A == B:
                return True
        return False
