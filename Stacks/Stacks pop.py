def pop(self):
    #if the stack is empty...
    if self.height == 0:
        return None
    temp = self.top
    self.top = self.top.next
    temp.next = None
    self.height -= 1
    return temp 