class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def size(self):
        return len(self.stack1) + len(self.stack2)

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(40)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())
print(queue.size())
