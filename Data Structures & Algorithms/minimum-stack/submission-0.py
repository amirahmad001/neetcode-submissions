class MinStack:

    def __init__(self):
        self.l = []
        
        

    def push(self, val: int) -> None:
        self.l.append(val)

    def pop(self) -> None:
        self.l = self.l[:-1]
        

    def top(self) -> int:
        return self.l[-1]
        

    def getMin(self) -> int:
        self.min_ = float('inf')
        for i in self.l:
            if i < self.min_:
                self.min_ = i
        return self.min_
        
