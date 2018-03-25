class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        skyline_lr = []
        for row in grid:
            skyline_lr.append(max(row))
        
        skyline_tb = []
        for i in range(len(grid[0])):
            column = []
            for j in range(len(grid)):
                column.append(grid[j][i])
            skyline_tb.append(max(column))
        
        incre = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                incre = min(skyline_lr[i], skyline_tb[j]) - grid[i][j] + incre
        
        return incre
        
