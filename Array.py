# Array.py

class Array:
    def __init__(self, initial=None):
        """Initialize the internal storage with an optional initial list."""
        if initial is None:
            self._data = []
        else:
            # Make a copy so external changes don't affect us
            self._data = list(initial)

    def append(self, value):
        """Add value to the end of the array."""
        # Uses Python list append (dynamic array behavior)
        self._data.append(value)

    def insert_at(self, index, value):
        """
        Insert value at given index.
        Elements at index and to the right are shifted one position to the right.
        """
        # Manual bounds check (so you understand behavior)
        if index < 0 or index > len(self._data):
            raise IndexError("insert_at index out of range")

        # --- Manual shifting version for learning ---
        self._data.append(None)  # extend the list by one dummy slot

        # shift elements to the right starting from the end
        for i in range(len(self._data) - 1, index, -1):
            self._data[i] = self._data[i - 1]

        # place the new value at index
        self._data[index] = value

    def delete_at(self, index):
        """
        Delete element at given index.
        Shift elements left to fill the gap.
        Return the removed value.
        """
        if index < 0 or index >= len(self._data):
            raise IndexError("delete_at index out of range")

        removed_value = self._data[index]

        # shift elements left from index+1 to end
        for i in range(index, len(self._data) - 1):
            self._data[i] = self._data[i + 1]

        # remove the now-duplicate last element
        self._data.pop()

        return removed_value

    def find(self, value):
        """
        Return the index of the first occurrence of value,
        or None if not found.
        """
        for i in range(len(self._data)):
            if self._data[i] == value:
                return i
        return None

    def __len__(self):
        """Return the number of elements in the array."""
        return len(self._data)

    def __str__(self):
        """Return a string like '[3, 6, 9]'."""
        return str(self._data)

    # Optional: let you index like a normal list: arr[0]
    def __getitem__(self, index):
        return self._data[index]

    # Optional: set by index: arr[0] = 10
    def __setitem__(self, index, value):
        self._data[index] = value