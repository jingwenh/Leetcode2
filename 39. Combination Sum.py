class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.target = target
        self.candidates = candidates
        self.candidates.sort()
        res = set()
        prefix = []
        self.dfs(res, prefix, 0)
        return list(res)
        
    
    def dfs(self, res, prefix, startIndex):
        if sum(prefix) > self.target:
            return
        elif sum(prefix) == self.target:
            temp = list(prefix)
            temp.sort()
            res.add(tuple(temp))
        elif sum(prefix) < self.target:
            for i, c in enumerate(self.candidates[startIndex:]):
                prefix.append(c)
                self.dfs(res, prefix, i)
                prefix.remove(c)
