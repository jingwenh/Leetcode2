# 用'abc'表示切开s的方式， 比如‘369’表示s[:3] + s[3:6] + s[6:9] + s[9:]
# 生成所有的切分方式，然后验证这种切分是不是符合ip地址的要求
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        
        self.all_division = []
        self.s = s
        self.dfs("")
        res = []
        for d in self.all_division:
            a = int(d[0])
            b = int(d[1])
            c = int(d[2])
            ip_addr = s[:a] + '.' + s[a:b] + '.' + s[b:c] + '.' + s[c:]
            if self.validAddr(ip_addr) == True:
                res.append(ip_addr)
        return res
        
    def dfs(self, prefix):
        if len(prefix) == 3:
            self.all_division.append(prefix)
            return
        if len(prefix) == 2:
            b = int(prefix[-1])
            for i in range(b + 1, len(self.s)):
                self.dfs(str(prefix + str(i)))
        if len(prefix) == 1:
            a = int(prefix[-1])
            for i in range(a + 1, len(self.s) - 1):
                self.dfs(str(prefix + str(i)))
        if len(prefix) == 0:
            for i in range(1, len(self.s) - 2):
                self.dfs(str(prefix + str(i)))
    
    def validAddr(self, s):
        subs = s.split('.')
        for sub in subs:
            if len(sub) == 0: 
                return False
            if len(sub) > 1 and sub[0] == '0':
                return False
            if int(sub) < 0 or int(sub) > 255:
                return False
        return True
                
                
