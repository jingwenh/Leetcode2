# 生成pattern 比较pattern， 类似205. Isomorphic Strings
from collections import OrderedDict
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        tokens = str.split(" ")
        return self.getPattern(tokens) == self.getPattern(pattern)
        
    def getPattern(self, tokens):
        dic = OrderedDict()
        for i, t in enumerate(tokens):
            dic[t] = 0
        l = list(dic.keys())
        s = ""
        for t in tokens:
            s = s + str(l.index(t))
        return s
