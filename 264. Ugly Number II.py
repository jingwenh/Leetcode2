# //生成丑数的方法：
# //更大的丑数 = 任意一个丑数 * 2 或 任意一个丑数 * 3 或 任意一个丑数 * 5
# //用小的丑数生成大的丑数，先放进HashSet里去重（是不是已经生成过了），再放进PriorityQueue里
# //每次从PriorityQueue里Poll出最小的那一个
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        pq = [1, 2, 3, 5]
        s = set([1, 2, 3, 5])
        
        count = 0
        for _ in range(n):
            next = heapq.heappop(pq)
            for i in (2, 3, 5):
                if i * next not in s:
                    heapq.heappush(pq, i * next)
                    s.add(i * next)
        return next
