class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.delta = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        self.grid = grid
        self.visited = set()
        self.areas = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    self.bfs((i, j))
        if len(self.areas):
            return max(self.areas)
        else:
            return 0
        
    def bfs(self, origin):
        q = []
        q.append(origin)
        # self.grid[origin[0]][origin[1]] = 0
        
        area = 0
        while len(q) > 0:
            cur = q.pop()
            if cur in self.visited:
                continue
            else:
                self.visited.add(cur)
            self.grid[cur[0]][cur[1]] = 0
            area = area + 1
            for d in self.delta:
                next = (cur[0] + d[0], cur[1] + d[1])
                if self.inBound(next) == True and self.grid[next[0]][next[1]] == 1:
                    q.append(next)
                    # self.grid[next[0]][next[1]] = 0
        self.areas.append(area)
        
    def inBound(self, coo):
        if coo[0] >= 0 and coo[0] < len(self.grid) and coo[1] >= 0 and coo[1] < len(self.grid[0]):
            return True
        return False
