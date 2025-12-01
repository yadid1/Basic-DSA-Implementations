# Queue.py

class Queue:
    def __init__(self, capacity=10):
        self._data = [None] * capacity
        self._capacity = capacity
        self._front = 0
        self._rear = 0
        self._size = 0

    def enqueue(self, value):
        """Add value to the end of the queue."""
        if self._size == self._capacity:
            raise Exception("Queue is full")

        self._data[self._rear] = value
        self._rear = (self._rear + 1) % self._capacity
        self._size += 1

    def dequeue(self):
        """Remove and return the front value."""
        if self.is_empty():
            return None

        value = self._data[self._front]
        self._data[self._front] = None  
        self._front = (self._front + 1) % self._capacity
        self._size -= 1

        return value

    def front(self):
        """Return the front value without removing it."""
        if self.is_empty():
            return None
        return self._data[self._front]

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __str__(self):
        """Return a string of queue contents in order."""
        items = []
        index = self._front
        for _ in range(self._size):
            items.append(str(self._data[index]))
            index = (index + 1) % self._capacity
        return " <- ".join(items)