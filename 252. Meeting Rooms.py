# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        pq = []
        for i in intervals:
            heapq.heappush(pq, (i.start, i.end))
        
        while len(pq) > 0:
            i1 = heapq.heappop(pq)
            if len(pq) == 0:
                return True
            i2 = heapq.heappop(pq)
            if i2[0] < i1[1]:
                return False
            heapq.heappush(pq, i2)
        
        return True
        
