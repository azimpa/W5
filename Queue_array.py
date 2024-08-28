class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            return self.queue.pop(0)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            for item in self.queue:
                print(item, end="  ")
            print()


qa = Queue()
qa.enqueue(1)
qa.enqueue(2)
qa.enqueue(3)
qa.enqueue(4)
qa.display()
print()
print(qa.dequeue())
print()
qa.display()
