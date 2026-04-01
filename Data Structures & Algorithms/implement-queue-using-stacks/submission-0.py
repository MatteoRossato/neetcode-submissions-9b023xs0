class MyQueue:

    def __init__(self):
        self.myQueue = []

    def push(self, x: int) -> None:
        self.myQueue.append(x)

    def pop(self) -> int:
        tmp = self.myQueue[0]
        self.myQueue = self.myQueue[1:]
        return tmp

    def peek(self) -> int:
        return self.myQueue[0]

    def empty(self) -> bool:
        if len(self.myQueue) > 0:
            return False
        else:
            return True



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()