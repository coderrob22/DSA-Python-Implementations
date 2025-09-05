class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node 

# You can also set the root to empty, where there is no Node and it has to be inserted like so:

class BinarySearchTree2:
    def __init__(self):
        self.root = None 

#  This ^^ might be the more common way to implement the constuctor