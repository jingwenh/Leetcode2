# // 按运算符分治
# //定义diffWaysToCompute返回的是所有可能的运算结果
# // diffWaysToCompute = 运算符左边diffWaysToCompute所有可能结果 和 运算符右边diffWaysToCompute所有可能结果 按照分割符运算
# //按顺序找运算符，把算式切成左半边和右半边放进去递归
# //递归出口是输入只有数字没有运算符
class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = []
        # 用enumerate可以在遍历字符串的同时获得这个字符的索引
        for i, c in enumerate(input):
            if c in '+-*':
                left_res = self.diffWaysToCompute(input[:i])
                right_res = self.diffWaysToCompute(input[i+1:])
                for a in left_res:
                    for b in right_res:
                        res.append(eval(str(a) + str(c) + str(b)))
        
        # 经过循环res还是空的，说明input里没有运算符，只有单独一个数字，那直接把它放到res里
        if len(res) == 0:
            res.append(int(input))
        return res
                    
