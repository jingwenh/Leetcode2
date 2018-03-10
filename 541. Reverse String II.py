# 先按照2k长度切分字符串，再reverse，再拼起来
class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        split_by_2k = []
        prv = 0
        cur = 2 * k
        while prv < len(s):
            split_by_2k.append(s[prv:cur])
            prv = prv + 2 * k
            cur = cur + 2 * k
        
        for i, token in enumerate(split_by_2k):
            s1 = token[0:k][::-1] # reverse string
            s2 = token[k:]
            split_by_2k[i] = s1 + s2
        
        return ''.join(split_by_2k)
            
        
