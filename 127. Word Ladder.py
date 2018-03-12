# 把单词放进q，在wordList里找有没有只差一个字母的单词，有就放进Q
import string
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # print(wordList)
        
        wordList = set(wordList)
        
        q = []
        q.append([beginWord])
        if beginWord in wordList:
            wordList.remove(beginWord)
        # res_path = []
        
        while len(q) > 0:
            # print(q)
            cur_path = q.pop(0)
            cur_word = cur_path[-1]
            if cur_word == endWord:
                return len(cur_path)
            
            # 变换字母，查在不在词典里
            # print(wordList)
            for i, c in enumerate(cur_word):
                for letter in string.ascii_letters:
                    new_word = cur_word[0:i] + letter + cur_word[i+1:]
                    if new_word in wordList:
                        next_path = list(cur_path)
                        next_path.append(new_word)
                        q.append(next_path)
                        wordList.remove(new_word)
        return 0
