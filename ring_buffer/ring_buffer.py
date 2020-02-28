from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if not at full capacity, make new node
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        else:
            if self.current is None:
                self.current = self.storage.head

            self.current.value = item

            if self.current.next is not None:
                self.current = self.current.next
            else:
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        curr = self.storage.head
        while(curr is not None):
            list_buffer_contents.append(curr.value)
            curr = curr.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        self.storage[self.current] = item
        self.current += 1

        if self.current > self.capacity - 1:
            self.current = 0

    def get(self):
        temp_storage = []
        for item in self.storage:
            if item is not None:
                temp_storage.append(item)
        return temp_storage
