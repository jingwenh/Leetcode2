# Count the number of consecutive 0's and 1's
# 两个连续的0和1，生成的符合要求的字符串是0和1中数量较小的数量
# https://leetcode.com/problems/count-binary-substrings/discuss/108625/Python-easy-and-concise-solution-(only-2-lines)
class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Count consective 0 and 1
        count = []
        consecutive_bits = s.replace("10","1 0").replace("01", "0 1").split(" ")
        lens = [len(cb) for cb in consecutive_bits]
        
        # Count
        left = 0
        right = 1
        res = 0
        while right < len(lens):
            res = res + min(lens[left], lens[right])
            left = left + 1
            right = right + 1
        return res
