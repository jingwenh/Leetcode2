class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0        
        
        ns = heapq.nlargest(2, nums)
        if ns[1] * 2 <= ns[0]:
            return nums.index(ns[0])
        return -1
