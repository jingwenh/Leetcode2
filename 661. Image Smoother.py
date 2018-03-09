# 按顺序算就好了
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0)]
        self.M = M
        new_M = [[0 for x in range(len(M[0]))] for y in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                coo = (i, j)
                surrounding_sum = 0
                count = 0
                for d in delta:
                    new_coo = (coo[0] + d[0], coo[1] + d[1])
                    if self.inBound(new_coo):
                        surrounding_sum = surrounding_sum + M[new_coo[0]][new_coo[1]]
                        count = count + 1
                new_M[new_coo[0]][new_coo[1]] = int(surrounding_sum / count)
        return new_M
    
    def inBound(self, coo):
        if coo[0] >= 0 and coo[0] < len(self.M) and coo[1] >= 0 and coo[1] < len(self.M[0]):
            return True
        return False
        
