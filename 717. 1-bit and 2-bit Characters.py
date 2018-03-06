from collections import deque
# When reading from the i-th position, if bits[i] == 0, the next character must have 1 bit; else if bits[i] == 1, the next character must have 2 bits. We increment our read-pointer i to the start of the next character appropriately. At the end, if our pointer is at bits.length - 1, then the last character must have a size of 1 bit.
class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        cur = 0
        while cur < len(bits) - 1:
            if bits[cur] == 0:
                cur = cur + 1
            if bits[cur] == 1:
                cur = cur + 2
        
        # 游标停在bits的最后一位上说明多了一位
        return cur == len(bits) - 1
