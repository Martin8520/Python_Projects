class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.move_in_to_out()
        return self.out_stack.pop()

    def peek(self) -> int:
        self.move_in_to_out()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def move_in_to_out(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())  # 1
print(myQueue.pop())  # 1
print(myQueue.empty())  # False
