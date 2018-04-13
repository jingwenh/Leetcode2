# dfs, 走过的节点放进visited
class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = list(nums)
        self.res = []
        self.visited = set()
        for n in nums:
            if n in self.visited:
                continue
            if n < len(nums):
                self.dfs(n, set())
            
        max_len = -float('inf')
        for r in self.res:
            if len(r) > max_len:
                max_len = len(r)
        return max_len
        
    def dfs(self, idx, idx_set):
        if idx in idx_set or idx >= len(self.nums):
            self.res.append(idx_set)
            self.visited.update(idx_set)
            return          
        
        next_set = set(idx_set)
        next_set.add(idx)
        self.dfs(self.nums[idx], next_set)
