# 初始化：每个岛屿自成一块
# 先判断边的数量和点的关系是不是符合edges = nodes - 1，再判断有没有环
# 遍历edges进行合并操作
# 合并前如果发现两块岛屿已经是同一个father了，则说明是invalid的
class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        uf = UnionFind()
        for e in edges:
            uf.fathers[e[0]] = e[0]
            uf.fathers[e[1]] = e[1]
            
        for e in edges:
            if uf.union(e[0], e[1]):
                continue
            else:
                return False
        
        return len(edges) == n - 1 
        
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
