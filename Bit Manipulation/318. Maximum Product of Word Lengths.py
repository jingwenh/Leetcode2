# Incentive: 用32-bit串表示单词，第一位表示a, 第二位表示b，依次类推
# 比如：
# a = 00001
# b = 00010
# c = 00100
# abc = 00111
# 构造方法：
# 1. 先将字母转换成0-25的十进制数，再将1左移对应位数
# 比如c = 2, 则1左移2位得到0100
# 2. 将所有的字母的bit串用或操作拼接
# a = 0001, b = 0010, c = 0100, a | b | c = 0111
# 如果两个单词没有相同字母，bit串进行and操作得到全0串
class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) <= 1:
            return 0
        
        def toBits(s):
            f = lambda c : 1 << (ord(c) - ord('a'))
            res = 0
            for c in s:
                res = res | f(c)
            # print(bin(res))
            return res
        
        maximum = 0
        bits = list(map(toBits, words))
        for i in range(len(bits)):
            for j in range(1, len(bits)):
                if bits[i] & bits[j] == 0:
                    val = len(words[i]) * len(words[j])
                    maximum = max(maximum, val)
        
        return maximum
        
            
        
        
