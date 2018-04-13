# https://leetcode.com/problems/excel-sheet-column-title/discuss/51404/Python-solution-with-explanation
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        self.letters = []
        self.res = None
        for i in range(65, 91):
            self.letters.append(chr(i))
        
        remain = n
        word = ""
        while remain > 0:
            print(remain)
            word = self.letters[(remain - 1) % 26] + word # 用remain - 1可以使得余数为0 - 25
            remain = int((remain - 1) / 26)
        return word
