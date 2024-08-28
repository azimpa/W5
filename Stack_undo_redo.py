class UndoRedo:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
        self.current_state = None

    def perform_operation(self, new_state):
        if self.current_state is not None:
            self.undo_stack.append(self.current_state)
        self.current_state = new_state
        # Clear the redo stack because we are making a new operation
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            print("No operations to undo.")
            return
        self.redo_stack.append(self.current_state)
        self.current_state = self.undo_stack.pop()

    def redo(self):
        if not self.redo_stack:
            print("No operations to redo.")
            return
        self.undo_stack.append(self.current_state)
        self.current_state = self.redo_stack.pop()

    def get_current_state(self):
        return self.current_state


history = UndoRedo()
# Initial state
history.perform_operation("State 1")
print(history.get_current_state())  # Output: State 1
# Perform some operations
history.perform_operation("State 2")
print(history.get_current_state())  # Output: State 2
history.perform_operation("State 3")
print(history.get_current_state())  # Output: State 3
# Undo operations
history.undo()
print(history.get_current_state())  # Output: State 2
history.undo()
print(history.get_current_state())  # Output: State 1
# Redo operations
history.redo()
print(history.get_current_state())  # Output: State 2

history.redo()
print(history.get_current_state())  # Output: State 3
