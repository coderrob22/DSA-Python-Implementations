class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
