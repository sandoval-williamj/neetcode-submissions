class MinStack:
    def __init__(self):
        self.my_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.my_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.my_stack.pop()
        if self.min_stack[-1] == val:
            self.min_stack.pop()


    def top(self) -> int:
        return self.my_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
