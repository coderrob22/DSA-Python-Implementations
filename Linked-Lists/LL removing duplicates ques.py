def remove_duplicates(self):
    values = set()
    previous = None
    current = self.head
    while current:
        if current.value in values:
            previous.next = current.next
            self.length -= 1
        else:
            values.add(current.value)
            previous = current
        current = current.next

