# 每个点自成一个集合
# 每加入一个节点，看上下左右有没有岛屿，有就把岛屿合并
# 合并前一定要记得判断双方是不是同一个father
class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        self.island_count = 0 # 每新建一个岛++，每次union--
        self.fathers = dict()
        self.m = m
        self.n = n
        
        mat = [[0 for i in range(n)] for j in range(m)]
        res = []
        
        for i in range(m):
            for j in range(n):
                self.fathers[(i, j)] = (i, j)
        
        for pos in positions:
            self.island_count = self.island_count + 1
            cur = (pos[0], pos[1])
            mat[cur[0]][cur[1]] = 1
            for d in delta:
                neighbor = (cur[0] + d[0], cur[1] + d[1])
                # 合并前要判断新加的一块和周围的四块是不是同一个father, 同一个father就不能做union（本来就属于那一块）
                # case: 3, 3, [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]
                if self.inbound(neighbor) and mat[neighbor[0]][neighbor[1]] == 1 and self.sameFather(neighbor, cur) == False:
                    self.union(cur, neighbor)
            res.append(self.island_count)
        
        return res
                
    def union(self, son1, son2):
        father1 = self.find(son1)
        father2 = self.find(son2)
        self.fathers[father1] = father2
        self.island_count = self.island_count - 1
    
    def find(self, son):
        if self.fathers[son] == son:
            return son
        else:
            self.fathers[son] = self.find(self.fathers[son])
            return self.fathers[son]
    
    def sameFather(self, son1, son2):
        father1 = self.find(son1)
        father2 = self.find(son2)
        if father1 == father2:
            return True
        return False
        
        
    def inbound(self, coo):
        if coo[0] >= 0 and coo[0] < self.m and coo[1] >= 0 and coo[1] < self.n:
            return True
        return False
