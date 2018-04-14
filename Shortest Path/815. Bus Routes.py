class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        
        self.res = []
        self.routes_dic = dict()
        self.T = T
        self.S = S
        starts = []
        for i, r in enumerate(routes):
            self.routes_dic[i] = set(r)
            if S in r:
                starts.append(i)
        
        for i in starts:
            self.takeBus(set([i]), set(self.routes_dic[i]))
        try:
            return min(self.res)
        except:
            return -1
   
    # 深搜，如果没坐过的bus和当前的bus路线有交集就递归，到达终点退出，最后返回最少换乘数量
    def takeBus(self, bus_taken, cur):
        # print(cur)
        if self.T in cur:
            self.res.append(len(bus_taken))
            return
        for k, v in self.routes_dic.items():
            if k not in bus_taken and len(set.intersection(cur, v)) != 0:
                new_bus_taken = set(bus_taken)
                new_bus_taken.add(k)
                self.takeBus(new_bus_taken, set(v))

    # BFS层序遍历，记录层数，找到T的那一层返回当前层数
    # 如果没坐过的bus和当前的bus路线有交集就递归，到达终点退出，最后返回最少换乘数量
    class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        
        self.res = []
        self.routes_dic = dict()
        self.T = T
        self.S = S
        q = []
        for i, r in enumerate(routes):
            self.routes_dic[i] = set(r)
            if S in r:
                q.append(i)
        
        count = 0
        bus_taken = set()
        
        while len(q) > 0:
            size = len(q)
            count = count + 1
            for i in range(size):
                cur = q.pop(0)
                if cur not in bus_taken:
                    bus_taken.add(cur)
                else:
                    continue
                if T in self.routes_dic[cur]:
                    self.flag = True
                    return count                
                for k, v in self.routes_dic.items():
                    if len(set.intersection(self.routes_dic[cur], v)) > 0:
                        q.append(k)
            
        return -1
