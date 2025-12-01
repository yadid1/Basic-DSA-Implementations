# Basic-DSA-Implementations
Basic DSA Implementations 
Overview

This project implements four core data structures from scratch in Python to demonstrate understanding of memory management, pointer manipulation, and time complexity.
Each structure includes a driver file showing required test operations.

⸻

Part A — Array (Wrapper)

Files: Array.py, test_Array.py
Features:
	•	append(value)
	•	insert_at(index, value)
	•	delete_at(index)
	•	find(value)
	•	__len__(), __str__()

Test: Start with [3, 6, 9], append 12, insert 4 at index 1, delete index 2.

⸻

Part B — Singly Linked List

Files: LinkedList.py, test_LinkedList.py
Features:
	•	insert_at_head(value)
	•	insert_at_tail(value)
	•	delete_first(value)
	•	find(value)
	•	__str__()

Test: Build 10 → 20 → 30, insert 15 at head, insert 40 at tail, delete 20.

⸻

Part C — Stack (LIFO)

Files: Stack.py, test_Stack.py
Implementation: Uses the Linked List (head = top).
Features:
	•	push(value)
	•	pop()
	•	peek()
	•	is_empty()
	•	__len__(), __str__()

Test: Push 10, 20, 30 → peek → pop twice → print remaining.

⸻

Part D — Queue (FIFO)

Files: Queue.py, test_Queue.py
Implementation: Circular array using front, rear, and size.
Features:
	•	enqueue(value)
	•	dequeue()
	•	front()
	•	is_empty()
	•	__len__(), __str__()

Test: Enqueue 5, 10, 15, 20 → dequeue twice → print remaining.

⸻

How to Run Tests
python test_Array.py
python test_LinkedList.py
python test_Stack.py
python test_Queue.py

Time Complexity (Summary)
	•	Array insert/delete: O(n)
	•	Linked list head operations: O(1)
	•	Stack push/pop: O(1)
	•	Queue enqueue/dequeue (circular array): O(1)
