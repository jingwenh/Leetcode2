# 初始化：每个岛屿自成一块
# 遍历edges进行合并操作
# 合并前如果发现两块岛屿已经是同一个father了，则说明是redundant的
class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        uf = UnionFind()
        res = []
        for e in edges:
            uf.fathers[e[0]] = e[0]
            uf.fathers[e[1]] = e[1]
        for e in edges:
            if uf.union(e[0], e[1]):
                continue
            else:
                res.append(e)
        return res[-1]

class UnionFind:
    def __init__(self):
        self.fathers = dict()
    
    def find(self, son):
        if self.fathers[son] == son:
            return son
        else:
            self.fathers[son] = self.find(self.fathers[son])
            return self.fathers[son]
    
    def union(self, son1, son2):
        father1 = self.find(son1)
        father2 = self.find(son2)
        if father1 != father2:
            self.fathers[father1] = father2
            return True
        else:
            return False
        
