class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def set_item(self, key, value):
        # find the index
        index = self.__hash(key)
        # if the address table is empty then set the list item inside the index
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])