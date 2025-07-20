def remove(self, index):
    # this is for if the remove is outside of the list
    if index < 0 or index >= self.length:
        return None
    # if the remove is for the first index, use the pop first method
    if index == 0:
        return self.pop_first()
    # if the remove is the last index, use the pop method
    if index == self.length - 1:
        return self.pop()
    
    prev = self.get(index-1)
    temp = prev.next
    prev.next = temp.next
    temp.next = None
    self.length -= 1
    return temp 
