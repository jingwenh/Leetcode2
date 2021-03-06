# 把log放进字典里，key = message， value=上一次打印的timestamp
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log = dict()
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.log:
            self.log[message] = timestamp
            return True
        else:
            lastPrintTime = self.log[message]
            if timestamp - lastPrintTime >= 10:
                self.log[message] = timestamp
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
