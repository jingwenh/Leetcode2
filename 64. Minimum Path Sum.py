class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.paths = []
        self.moves = {(1, 0), (0, 1)}
        self.dfs(grid, (0, 0), [])
        
        # print(self.paths)
        
        path_sum = float('inf')
        for path in self.paths:
            s = sum(path)
            if s < path_sum:
                path_sum = s
        return path_sum
    
    def dfs(self, grid, cur, prefix):
        # print(cur)
        prefix.append(grid[cur[0]][cur[1]])
        
        if cur == (len(grid) - 1, len(grid[0]) - 1):
            self.paths.append(list(prefix))
            return
        for move in self.moves:
            next = (cur[0] + move[0], cur[1] + move[1])
            if next[0] >= 0 and next[1] >= 0 and next[0] < len(grid) and next[1] < len(grid[0]):
                self.dfs(grid, next, prefix)
                prefix.remove(grid[next[0]][next[1]])
            
            
            
