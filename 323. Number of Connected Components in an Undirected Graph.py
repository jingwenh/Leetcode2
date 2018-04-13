# 初始化：每块岛屿自成一块
# 然后根据edge合并每块岛屿
class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf = UnionFind()
        for e in edges:
            uf.father[e[0]] = e[0]
            uf.father[e[1]] = e[1]
        
        unconn_nums = n - len(uf.father.keys())
        
        for e in edges:
            uf.union(e[0], e[1])
        
        res = 0
        for k, v in uf.father.items():
            if k == v:
                res = res + 1
        
        return res + unconn_nums
                
class UnionFind:
    def __init__(self):
        self.father = dict()
    
    def find(self, son):
        if self.father[son] == son:
            return son
        else:
            self.father[son] = self.find(self.father[son])
            return self.father[son]
    
    def union(self, son1, son2):
        father1 = self.find(son1)
        father2 = self.find(son2)
        if father1 != father2:
            self.father[father1] = father2
