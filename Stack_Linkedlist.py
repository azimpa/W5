class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack is empty")
        else:
            data = self.head.data
            self.head = self.head.next
            return data

    def peek(self):
        if self.head is None:
            print("Stack is empty")
        else:
            return self.head.data

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
            print("Stack is empty")
        else:
            current = self.head
            while current:
                print(current.data, "-->", end=" ")
                current = current.next
            print()

    def rev(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


st = Stack()
st.push(34)
st.push(38)
st.push(31)
st.display()

print(st.peek())

print(st.pop())

print(st.search(38))

st.display()

st.rev()
st.display()
