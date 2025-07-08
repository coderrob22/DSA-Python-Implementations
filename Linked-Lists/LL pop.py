def pop(self):
    # If LinkedList is empty, do this
    if self.length == 0:
        return None
    
    # Use this for all other cases
    temp = self.head
    pre = self.head

    while(temp.next):
        pre = temp
        temp = temp.next

    self.tail = pre
    self.tail.next = None
    self.length -= 1

    # Use this if only 1 number in the list
    if self.length == 0:
        self.head = None
        self.tail = None
    return temp