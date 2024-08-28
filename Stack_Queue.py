class Stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, item):
        while self.queue1:
            self.queue2.append(self.queue1.pop(0))

        self.queue1.append(item)

        while self.queue2:
            self.queue1.append(self.queue2.pop(0))

    def pop(self):
        if not self.queue1:
            return "Stack is empty"
        
        return self.queue1.pop(0)

    def peek(self):
        if not self.queue1:
            return "Stack is empty"

        return self.queue1[0]

    def is_empty(self):
        return not self.queue1
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.peek())
print(stack.is_empty())
