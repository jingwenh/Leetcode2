class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        res = heapq.nlargest(3, nums)
        if len(res) == 3:
            return res[-1]
        else:
            return res[0]
