class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else: 
            return self.stack.pop()  

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack[-1]

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            for item in self.stack:
                print(item, end=" ")
            print()    

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display() 

stack.pop()
stack.display()



print(stack.peek())

print(stack.is_empty())

