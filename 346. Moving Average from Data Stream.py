from collections import deque
class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.d = deque()
        self.size = size
        self.presum = 0
        
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.d) < self.size:
            self.d.append(val)
            self.presum = self.presum + val
            return self.presum / len(self.d)
        else:
            pop = self.d.popleft()
            self.presum = self.presum - pop
            self.d.append(val)
            self.presum = self.presum + val
            return self.presum / len(self.d)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
