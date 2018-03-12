# Cows: match the secret number but locate in the wrong position 
# 用HashMap存secret
# 先找A，每找到一个数map对应的value--
# 再找B，每找到一个数map对应的value--
from collections import Counter
class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        secret_map = dict(Counter(secret))
        
        A = 0
        remains = list(guess)
        for i, n in enumerate(guess):
            if n == secret[i]:
                A = A + 1
                remains[i] = '.'
                secret_map[n] = secret_map[n] - 1
        
        B = 0
        for n in remains:
            if n in secret_map.keys() and secret_map[n] > 0:
                B = B + 1
                secret_map[n] = secret_map[n] - 1
        
        return str(A) + 'A' + str(B) + 'B'
