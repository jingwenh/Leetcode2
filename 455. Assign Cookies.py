# 先搞定容易满足的小孩
# 按顺序从小到大给饼干
class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        
        res = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res = res + 1
                i = i + 1 # 满足了，换下一个孩子
            j = j + 1 #当前最容易满足的孩子都满足不了，换更大的饼干
        
        return res
