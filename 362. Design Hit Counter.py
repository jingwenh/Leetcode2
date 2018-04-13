class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = dict()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if timestamp in self.hits:
            self.hits[timestamp] = self.hits[timestamp] + 1
        else:
            self.hits[timestamp] = 1
        print(self.hits)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        res = 0
        for k, v in self.hits.items():
            if timestamp - k < 300:
                res = res + self.hits[k]
        return res
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
