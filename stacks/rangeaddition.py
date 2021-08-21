class RangeStack:

    def __init__(self) -> None:
        self.stack = []
        self.add = []
        self.cursum = 0

    def push(self, v : int) -> None:
        self.cursum += v
        self.stack.append(v)
        self.add.append(0)

    def pop(self) -> int:
        if not self.add: 
            return -1
        
        if len(self.add) > 1:
            self.add[-2] += self.add[-1]

        val = self.stack.pop() + self.add.pop()
        self.cursum -= val
        return val
    
    def inc(self, i : int, v : int) -> None:
        if self.add:
            id = min(i, len(self.add)) - 1
            self.add[id] += v
        
        self.cursum += i * v
    
    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False
    
    def peek(self) -> int:
        if self.add:
            return self.stack[-1] + self.add[-1]
        return self.stack[-1]
    
    def sum(self) -> int:
        return self.cursum
