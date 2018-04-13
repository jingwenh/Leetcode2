class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        uf = UnionFind()
        
        for n in nums:
            uf.father[n] = n
        
        # 如果n - 1或n + 1在father里，就把两个数union
        for n in nums:
            if (n - 1) in uf.father:
                uf.union(n - 1, n)
            if (n + 1) in uf.father:
                uf.union(n + 1, n)       
        
        # Compress all, 让属于同一个序列的数都指向同一个father
        for n in nums:
            uf.find(n)
                
        # 把father一样的entry合并到一起
        combine_father = dict()
        for k, v in uf.father.items():
            if v in combine_father:
                combine_father[v].append(k)
            else:
                combine_father[v] = []
                combine_father[v].append(k)

        # print(uf.father)
        # print(combine_father)
        
        max_len = 0
        for v in combine_father.values():
            if len(v) > max_len:
                max_len = len(v)
        return max_len

class UnionFind:
    def __init__(self):
        self.father = dict()

    def find(self, son):
        cur = son
        while self.father[cur] != cur:
            cur = self.father[cur]
        daddy = cur
        cur = son
        while self.father[cur] != cur:
            tmp = cur
            cur = self.father[cur]
            self.father[tmp] = daddy
        return daddy
        
    def union(self, son1, son2):
        f1 = self.find(son1)
        f2 = self.find(son2)
        if f1 != f2:
            self.father[f1] = f2
