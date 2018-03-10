from collections import OrderedDict
class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]
        
        init = ''.join(['0'] * n)
        self.codes = OrderedDict()
        self.codes[init] = 0
        self.n = n
        self.dfs()
        
        res = []
        for code in self.codes.keys():
            res.append(int(code, 2))
        
        return res
        
    def dfs(self):
        if len(self.codes.keys()) == pow(2, self.n):
            return
        prv = list(self.codes.keys())[-1]
        for i, c in enumerate(prv):
            if c == '0':
                next_code = prv[:i] + '1' + prv[i+1:]
                if next_code not in self.codes.keys():
                    self.codes[next_code] = 0
                    self.dfs()
                    break
            if c == '1':
                next_code = prv[:i] + '0' + prv[i+1:]
                if next_code not in self.codes.keys():
                    self.codes[next_code] = 0
                    self.dfs()
                    break        
