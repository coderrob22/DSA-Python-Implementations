def set_value(self, index, value):
    temp = self.get(index)

    if temp: #if temp is not None 
        temp.value = value
        return True
    return False