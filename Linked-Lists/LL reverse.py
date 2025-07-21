def reverse(self):
    # create a new variable 'temp', and then switch head and tail around
    temp = self.head
    self.head = self.tail
    self.tail = temp

    # create a 'before' and 'after' variable to track before and after temp
    after = temp.next
    before = None

    for _ in range(self.length):
        after = temp.next
        temp.next = before
        before = temp
        temp = after