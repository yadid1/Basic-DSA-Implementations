# Stack.py

from LinkedList import LinkedList

class Stack:
    def __init__(self):
        self._list = LinkedList()
        self._size = 0

    def push(self, value):
        """Push value onto the stack (insert at head)."""
        self._list.insert_at_head(value)
        self._size += 1

    def pop(self):
        """Remove and return the top value."""
        if self.is_empty():
            return None  # or raise exception

        value = self._list.head.data
        self._list.delete_first(value)  # delete head

        self._size -= 1
        return value

    def peek(self):
        """Return the top value without removing."""
        if self.is_empty():
            return None
        return self._list.head.data

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __str__(self):
        """Print from top to bottom."""
        return f"Top -> {self._list}"