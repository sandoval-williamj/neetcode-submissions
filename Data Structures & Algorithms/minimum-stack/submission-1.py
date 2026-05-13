class MinStack:
    def __init__(self):
        self.my_stack = []

    def push(self, val: int) -> None:
        self.my_stack.append(val)

    def pop(self) -> None:
        self.my_stack.pop()

    def top(self) -> int:
        return self.my_stack[-1]

    def getMin(self) -> int:
        mini = self.my_stack[0]
        for i in self.my_stack:
            mini = min(i, mini)
        return mini
        
