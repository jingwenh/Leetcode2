# 拿一个set存前缀
# 将words排序(先按字母排，再按长度排，短的在前长的在后)，遍历words
# 将word删去最后一个字母得到前缀，看set里有没有这个前缀，有就把这个word放进去
class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        prefixes = set()
        prefixes.add('')
        
        for word in sorted(words):
            if word[:-1] in prefixes:
                prefixes.add(word)
        
        prefixes = list(prefixes)
        prefixes.sort(key=len)
        max_len = len(prefixes[-1])
        
        res = []
        for w in prefixes:
            if max_len == len(w):
                res.append(w)
        
        return sorted(res)[0]
