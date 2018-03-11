from collections import deque
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candidates = sorted(candidates)
        self.target = target
        self.res = set()
        self.dfs([], 0)
        return list(self.res)
    
    def dfs(self, prefix, start):
        if sum(prefix) > self.target:
            return
        if sum(prefix) == self.target:
            self.res.add(tuple(prefix))
            return
        for i in range(start, len(self.candidates)):
            next_prefix = list(prefix)
            next_prefix.append(self.candidates[i])
            self.dfs(next_prefix, i + 1)
            
            
