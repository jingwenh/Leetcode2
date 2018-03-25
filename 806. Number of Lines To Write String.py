class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 1
        cur = 0
        for c in S:
            units = widths[ord(c) - 97]
            if cur + units <= 100:
                cur = cur + units
            else:
                cur = units
                lines = lines + 1
        return [lines, cur]
