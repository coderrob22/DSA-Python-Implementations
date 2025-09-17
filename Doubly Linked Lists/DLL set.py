def set_value(self, value, index):
    temp = self.get(index)
    if temp:
        temp.value = value
        return True
    return False