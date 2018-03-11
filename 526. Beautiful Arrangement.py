# 生成所有的arrangements，如果不符合要求就跳过
class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.res = []
        self.N = N
        self.remaining_digits = set(range(1, N + 1))
        self.dfs([])
        return len(self.res)
    
    def dfs(self, prefix):
        if len(prefix) == self.N:
            self.res.append(prefix)
            return
        for i in self.remaining_digits:
            next_index = len(prefix) + 1
            if i % next_index == 0 or next_index % i == 0:
                next_prefix = list(prefix)
                next_prefix.append(i)
                self.remaining_digits.remove(i)
                self.dfs(next_prefix)
                self.remaining_digits.add(i)
            else:
                continue
