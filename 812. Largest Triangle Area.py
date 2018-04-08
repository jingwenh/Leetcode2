import math
class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        
        area = -float('inf')
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    if self.getArea(points[i], points[j], points[k]) > area:
                        area = self.getArea(points[i], points[j], points[k])
                
        return area
        
    
    def getArea(self, p1, p2, p3):
        try:
            a = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
            b = math.sqrt((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2)
            c = math.sqrt((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2)
            p = (a + b + c) / 2
            s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        except:
            return -1
        return s
    
