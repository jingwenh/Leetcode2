# 从最低位开始按顺序判断是不是1（&1判断）
# res左移一位，空出一位0来
# 如果是1，那在res的最后一位加0
# 如果是0，那在res的最后一位加1
# 然后将n右移

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = res << 1
            if n & 1 == 1: # 最后一位是0
                res = res | 1
            n = n >> 1
        return res
        
