# 不能被X围住的O = 边界上的O, 所有和边界上的O相连的O都不能被X围住
# 解法：先找所有和边界上O相连的O，然后标记这些O；把剩下的O都变成X；最后把标记的O变回O
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        
        def inbound(c):
            if c[0] >= 0 and c[0] < len(board) and c[1] >= 0 and c[1] < len(board[0]):
                return True
            return False
        
        def bfs(start):
            delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            q = []
            q.append(start)
            while len(q) != 0:
                cur = q.pop(0)
                board[cur[0]][cur[1]] = '+'
                
                for d in delta:
                    next_pos = (cur[0] + d[0], cur[1] + d[1])
                    if inbound(next_pos) == True and board[next_pos[0]][next_pos[1]] == 'O':
                        q.append(next_pos)
        
        for i in range(len(board)):
            if board[i][0] == 'O':
                bfs((i, 0))
            if board[i][-1] == 'O':
                bfs((i, len(board[0]) - 1))
                
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                bfs((0, i))
            if board[-1][i] == 'O':
                bfs((len(board) - 1, i))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '+':
                    board[i][j] = 'O'       
