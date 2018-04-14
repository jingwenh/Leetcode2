# BFS算最短路径记得要分层, 最短路径的长度实际上是层数

class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = []
        q.append(n)
        
        count = -1 # 第一个数不算
        while len(q) > 0:
            size = len(q)
            count = count + 1
            for i in range(size):
                cur = q.pop(0)
                if cur == 1:
                    return count
                if cur % 2 == 1:
                    q.append(cur + 1)
                    q.append(cur - 1)
                else:
                    q.append(cur / 2)
        return -1
