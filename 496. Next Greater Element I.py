# 用一个HashMap做预处理，key = num in nums2, value = first greater num at its right
# 构造Map需要用到Stack
# 遍历nums2，如果当前的数大于栈顶的数，pop栈里所有小于当前遍历到的这个数的数，存进hashmap里做key，value是当前遍历到的这个数；最后把nums2的元素按顺序放进stack
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = dict()
        stk = []
        for n in nums2:
            while len(stk) > 0 and n > stk[-1]:
                key = stk.pop()
                value = n
                dic[key] = value
            stk.append(n)
        
        res = []
        for n in nums1:
            if n in dic:
                res.append(dic[n])
            else:
                res.append(-1)
        
        return res
