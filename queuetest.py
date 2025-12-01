# test_Queue.py

from queuefile import Queue

def main():
    q = Queue()

    # 1) Enqueue 5, 10, 15, 20
    q.enqueue(5)
    q.enqueue(10)
    q.enqueue(15)
    q.enqueue(20)
    print("After enqueuing 5,10,15,20:", q)

    # 2) Dequeue twice
    print("Dequeue:", q.dequeue())   # Expect 5
    print("Dequeue:", q.dequeue())   # Expect 10

    # 3) Print remaining
    print("Remaining queue:", q)     # Expect 15 <- 20
    print("Length:", len(q))         # Expect 2

if __name__ == "__main__":
    main()