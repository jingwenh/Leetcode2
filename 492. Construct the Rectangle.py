class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(math.sqrt(area))
        while area % w != 0 and w >= 1:
            w = w - 1
        return [int(area / w), w]
