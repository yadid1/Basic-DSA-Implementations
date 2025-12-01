# LinkedList.py

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        # Helpful for debugging
        return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        # Start with an empty list
        self.head = None
        self.tail = None

    def insert_at_head(self, value):
        """Insert a new node with given value at the beginning (head) of the list."""
        new_node = Node(value, next=self.head)

        # Move head to the new node
        self.head = new_node

        # If list was empty, tail should also point to new_node
        if self.tail is None:
            self.tail = new_node

    def insert_at_tail(self, value):
        """Insert a new node with given value at the end (tail) of the list."""
        new_node = Node(value)

        # If the list is empty, head and tail both become this node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # Otherwise, link current tail to new node and update tail
        self.tail.next = new_node
        self.tail = new_node

    def find(self, value):
        """
        Find the first node with the given value.
        Return the node or None if not found.
        """
        current = self.head
        while current is not None:
            if current.data == value:
                return current
            current = current.next
        return None

    def delete_first(self, value):
        """
        Delete the first node that contains 'value'.
        Return True if a node was deleted, False otherwise.
        """
        current = self.head
        previous = None

        while current is not None:
            if current.data == value:
                # Case 1: deleting the head
                if previous is None:
                    self.head = current.next
                else:
                    # Bypass the current node
                    previous.next = current.next

                # Case 2: if we deleted the tail, update tail
                if current is self.tail:
                    self.tail = previous

                return True

            previous = current
            current = current.next

        # Value not found
        return False

    def __str__(self):
        """Return a string like 'a -> b -> c' representing the list contents."""
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next

        return " -> ".join(values)