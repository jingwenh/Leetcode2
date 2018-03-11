# 先生成permutations，再sort，再返回第k个
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.n = n
        self.remaining_digits = set(range(1, n + 1))
        self.res = []
        self.dfs("")
        self.res.sort()
        return str(self.res[k - 1])
    
    def dfs(self, prefix):
        if len(prefix) == self.n:
            self.res.append(int(prefix))
            return
        for i in self.remaining_digits:
            next_prefix = prefix + str(i)
            self.remaining_digits.remove(i)
            self.dfs(next_prefix)
            self.remaining_digits.add(i)
        
