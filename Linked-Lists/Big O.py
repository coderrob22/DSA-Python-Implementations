###    Adding and Removing from a linked list    ###

# Adding to the end of a linked list just requires you to change the pointer to the new element being added and adjust the tail. O(1).

# Removing an integer is more steps. To remove an element the tail has to iterate through the nodes to find the pointer that was pointing to the the element BEFORE the one that was removed. For this reason it is O(n)


# Adding and removing an item from the front of the list is also O(1) since it doesn't matter how many items are in the list, the same number of operations will remove or add it, per each item.

# Adding/removing an item to the middle of a linked list & Looking up and item are all O(n), since you need to iterate through the list from head to the item.

# **** Use Linked List vs Lists when prepending an item to the head or pop first the item from the head. In those cases, Big O(1)

# ****** Use List vs Linked list when popping last item or Lookup by index. Since list is O(1) and LL is O(n) in those cases.