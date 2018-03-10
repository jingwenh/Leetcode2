# 用deque存nums
# 按顺序把数字放进stack，如果递增继续放，出现记录递增序列长度，递减清空stack再放入新数
from collections import deque
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stk = []
        len_list = []
        nums = deque(nums)
        while len(nums) > 0:
            i = nums.popleft()
            if len(stk) > 0:
                if i > stk[-1]:
                    stk.append(i)
                else:
                    len_list.append(len(stk))
                    stk = list()
                    stk.append(i)
            else:
                stk.append(i)
        len_list.append(len(stk))
        return max(len_list)
