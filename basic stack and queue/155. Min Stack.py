class MinStack:
    import math
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.monostack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.monostack or self.monostack[-1] >= val:
            self.monostack.append(val)

    def pop(self) -> None:
        if self.stack and self.monostack:
            cur = self.stack.pop()
            if cur == self.monostack[-1]:
                self.monostack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.monostack:
            return None
        return self.monostack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()