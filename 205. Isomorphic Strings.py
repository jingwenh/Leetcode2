# 用index替换字符生成一个pattern
# pattern相同说明isom
from collections import OrderedDict
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.getPattern(s) == self.getPattern(t)
    
    def getPattern(self, s):
        new_s = str(s)
        dic = OrderedDict()
        for c in s:
            dic[c] = 0
        l = list(dic.keys())
        for i, c in enumerate(l):
            new_s = new_s.replace(c, str(i))
        return new_s
        
