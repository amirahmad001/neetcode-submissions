class MinStack:

    def __init__(self):
        self.l = []
        self.minStack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.l.append(value)
        if not self.minStack:
            self.minStack.append(value)
        else:
            self.minStack.append(min(value, self.minStack[-1]))
        
        

    def pop(self):
        """
        :rtype: None
        """
        #self.l = self.l[:-1]
        self.l.pop()
        self.minStack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.l[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
        
