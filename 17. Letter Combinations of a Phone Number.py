class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        
        self.mapping = {
            '1':"1", '2':"abc", '3':"def", '4':"ghi",
            '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv",
            '9':"wxyz", '0':"0"
        }
        self.res = []
        self.digits = digits
        self.dfs(0, "")
        return self.res
    
    # dfs('23','') = dfs('3','a') + dfs('3', 'b') + dfs('3', 'c') 
    # 判断当前是哪个数字
    # 遍历这个数字的字母，添加到prefix上，然后生成的prefix递归给下一层
    def dfs(self, num_index, prefix):
        if len(prefix) == len(self.digits):
            self.res.append(prefix)
            return
        
        num = self.digits[num_index]
        letters = self.mapping[num]
        for c in letters:
            next_prefix = str(prefix) + c
            self.dfs(num_index + 1, next_prefix)
