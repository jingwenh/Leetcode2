class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.n = n
        self.k = k
        self.dfs(1, [])
        return self.res
        
    # k = 2, n = 3
    # dfs('1') = dfs('12') + dfs('13')
    def dfs(self, start, prefix):
        if len(prefix) == self.k:
            self.res.append(prefix)
        for i in range(start, self.n + 1):
            next_prefix = list(prefix)
            next_prefix.append(i)
            self.dfs(i + 1, next_prefix)
