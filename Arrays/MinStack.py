class MinStack:
    def __init__(self):
        self.stack = []
        self.top_index = -1
        self.minimum = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.top_index += 1
            self.stack.append(val)
            self.minimum = val

        elif val >= self.minimum:
            self.top_index += 1
            self.stack.append(val)

        else:
            temp = 2*val - self.minimum
            self.top_index += 1
            self.stack.append(temp)
            self.minimum = val

    def pop(self) -> None:
        if self.stack[self.top_index] < self.minimum:
            self.top_index -= 1
            self.minimum = 2*self.minimum - self.stack.pop()

        else:
            self.top_index -= 1
            self.stack.pop()

    def top(self) -> int:
        if self.stack[self.top_index] < self.minimum:
            return self.minimum
        
        else:
            return self.stack[self.top_index]

    def getMin(self) -> int:
        return self.minimum