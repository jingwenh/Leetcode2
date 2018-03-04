# 注意分数会有负数
class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        records = []
        for i in ops:
            if i == '+':
                records.append(sum(records[-2:]))
            elif i == 'C':
                records.pop() # Cancel the score of the last round
            elif i == 'D':
                records.append(2 * records[-1])
            else:
                records.append(int(i))
        return sum(records)
        
