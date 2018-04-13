# 两根指针同时从尾到头遍历两个字符串
# 两根指针都越界时才结束
# 否则越界的那位按0处理
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        cur1 = len(num1) - 1
        cur2 = len(num2) - 1
        
        carry = 0
        res = ""
        while cur1 >= 0 or cur2 >= 0:
            if cur1 < 0:
                digit = int(num2[cur2]) + carry
            elif cur2 < 0:
                digit = int(num1[cur1]) + carry
            else:
                digit = int(num1[cur1]) + int(num2[cur2]) + carry
            # 处理carry，有进位为1，无进位为0
            if digit >= 10:
                digit = digit - 10
                carry = 1
            else:
                carry = 0
            res = str(digit) + res
            cur1 = cur1 - 1
            cur2 = cur2 - 1
        if carry == 1:
            res = str(carry) + res
        return res
        
