class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # print(wordList)
        
        wordList = set(wordList)
        originWordList = set(wordList)
        
        q = []
        heapq.heappush(q, (1, [beginWord]))
        if beginWord in wordList:
            wordList.remove(beginWord)
        res_path = []
        
        while len(q) > 0:
            # print(res_path)
            cur_path = tuple(q[-1])[1]
            del q[-1]
            cur_word = cur_path[-1]
            if cur_word == endWord:
                heapq.heappush(res_path, (len(cur_path), list(cur_path)))
                wordList = set(originWordList)
                continue
            
            # 变换字母，查在不在词典里
            for i, c in enumerate(cur_word):
                for letter in string.ascii_letters:
                    new_word = cur_word[0:i] + letter + cur_word[i+1:]
                    used_words = set(cur_path)
                    if new_word in wordList and new_word != cur_word and new_word not in used_words: 
                        next_path = list(cur_path)
                        next_path.append(new_word)
                        heapq.heappush(q, (len(next_path), next_path))
                        wordList.remove(new_word)
                        
        if len(res_path) == 0:
            return []
        
        res = []
        shortest_len = res_path[0][0]
        for path in res_path:
            if path[0] == shortest_len:
                res.append(path[1])
        
        return res
        
