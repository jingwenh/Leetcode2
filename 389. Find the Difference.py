from collections import Counter
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count_s = dict(Counter(s))
        count_t = dict(Counter(t))
        
        for key, value in count_t.items():
            if key not in count_s:
                return key
            elif count_t[key] != count_s[key]:
                return key
        
        return None
        
