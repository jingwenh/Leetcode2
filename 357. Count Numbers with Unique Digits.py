class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        
        remaining_digits = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.res = set()
        self.n = n
        self.dfs('', remaining_digits)
        
        return len(self.res)
    
    def dfs(self, prefix, remaining_digits):
        if len(prefix) > 0:
            self.res.add(int(prefix))
        
        if len(prefix) == self.n:
            self.res.add(int(prefix))
            return 
        
        for i in remaining_digits:
            next_prefix = prefix + str(i)
            remaining_digits.remove(i)
            self.dfs(next_prefix, remaining_digits)
            remaining_digits.add(i)
