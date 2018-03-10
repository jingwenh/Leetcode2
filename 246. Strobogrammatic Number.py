#先把6换成9,9换成6，再reverse，如果和原来的数字相同，就返回True
class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        non_stro = [2, 3, 4, 5, 7]
        for n in non_stro:
            if str(n) in num:
                return False
        
        new_num = []
        for n in num:
            if n == '6':
                new_num.append('9')
            elif n == '9':
                new_num.append('6')
            else:
                new_num.append(n)
        new_num = ''.join(reversed(new_num))
        
        if new_num == num:
            return True
        return False
        
