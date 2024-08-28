class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
        else:
            current = self.head.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return current

    def search(self, value):
        count = 1
        current = self.head
        while current and current.data != value:
            count += 1
            current = current.next
        if current:
            return count
        else:
            return -1

    def display(self):
        if self.head is None:
            print("Queue is empty")
        else:
            current = self.head
            while current:
                print(current.data, "-->", end=" ")
                current = current.next
            print()


ql = Queue()

ql.enqueue(1)
ql.enqueue(2)
ql.enqueue(3)
ql.enqueue(4)
ql.display()
print()

print(ql.dequeue())
print()

ql.display()
print()

print(ql.search(2))
