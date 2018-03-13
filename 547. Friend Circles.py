# 从0到len(M)遍历，从每个人出发找所有朋友，找到以后做标记，最后结果数组里有几个不同标记就有几个朋友
# 一维的灌水法
from collections import Counter
class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.res = [-1 for i in range(len(M))]
        self.M = M
        for i in range(len(M)):
            if self.res[i] == -1:
                self.dfs(i, i)
        
        return len(Counter(self.res).keys())
        
    def dfs(self, start, mark):
        self.res[start] = mark
        directs = []
        for i, f in enumerate(self.M[start]):
            if f == 1 and self.res[i] == -1: 
                directs.append(i)
                
        for f in directs:
            self.dfs(f, mark)
