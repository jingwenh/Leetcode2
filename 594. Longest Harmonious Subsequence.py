# 先统计每次数字的数量
# 存成元组列表然后按照数字的值排序
# 用长度为2的移动窗口记录相差为1的两组数字的长度
from collections import Counter, OrderedDict
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict(Counter(nums))
        l = list(dic.items())
        l = heapq.nsmallest(len(l), l, key = lambda tpl : tpl[0])
        
        left = 0
        right = 1
        
        len_list = []
        while right < len(l):
            t1 = l[left]
            t2 = l[right]
            if t2[0] - t1[0] <= 1:
                len_list.append(t2[1] + t1[1])
            left = left + 1
            right = right + 1
        
        if len(len_list) == 0:
            return 0
        return max(len_list)
            
