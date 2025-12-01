#test_Array.py

from Array import Array

def main():
    # 1. Start with [3, 6, 9]
    arr = Array([3, 6, 9])
    print("Initial array:", arr)

    # 2. Append 12
    arr.append(12)
    print("After appending 12:", arr)

    # 3. Insert 4 at index 1
    arr.insert_at(1, 4)
    print("After inserting 4 at index 1:", arr)

    # 4. Delete the element at index 2
    removed = arr.delete_at(2)
    print(f"Deleted value at index 2: {removed}")
    print("After deletion:", arr)

    # 5. Print the final array and its length
    print("Final array:", arr)
    print("Final length:", len(arr))


if __name__ == "__main__":
    main()