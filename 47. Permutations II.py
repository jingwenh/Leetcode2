class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.end_length = len(nums)
        self.res = set()
        self.dfs([], nums)
        return list(self.res)
    
    def dfs(self, prefix, nums):
        if len(prefix) == self.end_length:
            self.res.add(tuple(prefix))
            return
        for i, n in enumerate(nums):
            next_prefix = list(prefix)
            next_prefix.append(n)
            next_nums = list(nums)
            del next_nums[i]
            self.dfs(next_prefix, next_nums)
