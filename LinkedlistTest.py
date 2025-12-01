# test_LinkedList.py

from LinkedList import LinkedList

def main():
    ll = LinkedList()

    # 1) Build the list 10 -> 20 -> 30
    ll.insert_at_tail(10)
    ll.insert_at_tail(20)
    ll.insert_at_tail(30)
    print("Initial list:", ll)      # Expect: 10 -> 20 -> 30

    # 2) Insert 15 at head and 40 at tail
    ll.insert_at_head(15)
    print("After inserting 15 at head:", ll)   # Expect: 15 -> 10 -> 20 -> 30

    ll.insert_at_tail(40)
    print("After inserting 40 at tail:", ll)   # Expect: 15 -> 10 -> 20 -> 30 -> 40

    # 3) Delete 20
    deleted = ll.delete_first(20)
    print("Deleted 20?", deleted)   # Expect: True
    print("After deleting 20:", ll) # Expect: 15 -> 10 -> 30 -> 40

    # 4) Final list
    print("Final list:", ll)


if __name__ == "__main__":
    main()