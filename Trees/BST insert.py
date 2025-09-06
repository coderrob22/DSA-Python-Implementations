def insert(self, value):
    new_node = Node(value)
    # If the tree is empty...
    if self.root is None:
        self.root = new_node
        return True
    # If the tree is not empty set up temp and the while loop
    temp = self.root
    while (True):
    # If the new node is equal to a value that is already on the tree....
        if new_node.value == temp.value:
            return False
    # If the new node's value is not on the BST then do this....
        if new_node.value < temp.value:
            if temp.left is None:
                temp.left = new_node
                return True
            temp = temp.left
        else:
            if temp.right is None:
                temp.right = new_node
                return True
            temp = temp.right