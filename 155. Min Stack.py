# 在stack里存元组
# (number, curMin), 这样min会保持在栈顶
# 每次push的时候都会根据栈顶元素计算当前的min
# 每次pop完就会恢复到之前的状态 
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stk) == 0 or x < self.getMin():
            self.stk.append((x, x))
        elif x >= self.stk[-1][1]:
            self.stk.append((x, self.getMin()))
        
    def pop(self):
        """
        :rtype: void
        """
        return self.stk.pop()[0]
        
    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stk[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
