class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        
        
        # 假设炸弹在每个格子里都可以放，并且炸弹只能往上下左右一个方向炸
        
        # 定义状态：up[i][j]表示炸弹在(i, j)向上炸能炸死几个敌人
        up = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        # 状态转移：
        # 如果i = 0, 有enemy up[0][j] = 1否则 = 0
        # up[i][j] = 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'W':
                    up[i][j] = 0
                    continue
                if i == 0 and grid[i][j] == 'E':
                    up[i][j] = 1
                elif i == 0 and grid[i][j] != 'E':
                    up[i][j] = 0
                elif i != 0 and grid[i][j] == 'E':
                    up[i][j] = up[i - 1][j] + 1
                else:
                    up[i][j] = up[i - 1][j]
        
        # 再分别假设只能炸下、左、右
        down = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        # 从最下一行开始遍历
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0])):
                if grid[i][j] == 'W':
                    down[i][j] = 0
                    continue
                if i == len(grid) - 1 and grid[i][j] == 'E':
                    down[i][j] = 1
                elif i == len(grid) - 1  and grid[i][j] != 'E':
                    down[i][j] = 0
                elif i != len(grid) - 1  and grid[i][j] == 'E':
                    down[i][j] = down[i + 1][j] + 1
                else:
                    down[i][j] = down[i + 1][j]      
        
        left = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'W':
                    left[i][j] = 0
                    continue
                if j == 0 and grid[i][j] == 'E':
                    left[i][j] = 1
                elif j == 0  and grid[i][j] != 'E':
                    left[i][j] = 0
                elif j != 0  and grid[i][j] == 'E':
                    left[i][j] = left[i][j - 1] + 1
                else:
                    left[i][j] = left[i][j - 1] 
                    
        right = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        # 从最右开始遍历
        for i in range(len(grid)):
            for j in range(len(grid[0]) - 1, -1, -1):
                if grid[i][j] == 'W':
                    right[i][j] = 0
                    continue
                if j == len(grid[0]) - 1 and grid[i][j] == 'E':
                    right[i][j] = 1
                elif j == len(grid[0]) - 1  and grid[i][j] != 'E':
                    right[i][j] = 0
                elif j != len(grid[0]) - 1  and grid[i][j] == 'E':
                    right[i][j] = right[i][j + 1] + 1
                else:
                    right[i][j] = right[i][j + 1]         
        
        # print(up)
        # print(down)
        # print(left)
        # print(right)
        
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 'E':
                    res.append(left[i][j] + right[i][j] + up[i][j] + down[i][j])
        try:
            return max(res)
        except:
            return 0
