# 问题的关键在于两个数的位数不同时如何比较
# 比如3和30, 3和33, 3和34
# 把两个数字拼起来, 比较怎么样拼比较大
# 比如: 3和30, 330 > 303, 3 > 30; 30和3, 303 < 330, 30 < 3
# 再比如: 3和34, 334 < 343, 34 > 3; 34和3, 343 > 334, 34 < 3
import functools
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 0 or (len(set(nums)) == 1 and nums[0] == 0):
            return "0"
        
        def compare(a, b):
            n1 = int(a + b)
            n2 = int(b + a)
            return n1 - n2
        
        nums = list(map(lambda x : str(x), nums))
        sorted_nums = sorted(nums, key = functools.cmp_to_key(compare), reverse = True)
        
        res = "".join(sorted_nums)
        
        return res
