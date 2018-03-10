from collections import Counter
class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = dict(Counter(nums))
        res = set()
        
        if k < 0:
            return 0
        
        if k == 0:
            count = 0
            for k, v in dic.items():
                if v >= 2:
                    count = count + 1
            return count
        
        for i in nums:
            c1 = i + k
            c2 = i - k
            if c1 in dic.keys():
                res.add((i, c1))
            if c2 in dic.keys():
                res.add((c2, i))
        return len(res)
        
