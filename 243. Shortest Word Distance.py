class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # construct an index array for every word
        dic = dict()
        for i, w in enumerate(words):
            if w not in dic:
                dic[w] = [i]
            else:
                dic[w].append(i)
        
        # Find min diff between two index arrays
        res = float("inf")
        for i in dic[word1]:
            for j in dic[word2]:
                dif = abs(i - j)
                res = min(res, dif)
                
        
        return res
        
