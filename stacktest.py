# test_Stack.py

from stack import Stack

def main():
    s = Stack()

    # 1) Push 10, 20, 30
    s.push(10)
    s.push(20)
    s.push(30)
    print("After pushing 10,20,30:", s)   # Expect: Top -> 30 -> 20 -> 10

    # 2) Peek
    print("Peek top:", s.peek())           # Expect: 30

    # 3) Pop twice
    print("Pop:", s.pop())                 # Expect: 30
    print("Pop:", s.pop())                 # Expect: 20

    # 4) Print remaining elements
    print("Remaining stack:", s)           # Expect: Top -> 10
    print("Stack size:", len(s))           # Expect: 1

if __name__ == "__main__":
    main()