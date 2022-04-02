class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        
        print(self.stack2 , self.stack1)
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        print(self.stack2 , self.stack1)
        self.stack1.append(x)
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())
        print(self.stack2 , self.stack1)
        
    def pop(self) -> int:
        if(self.stack1 != []):
            return self.stack1.pop()
        return []

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        if(self.stack1 != []):return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()