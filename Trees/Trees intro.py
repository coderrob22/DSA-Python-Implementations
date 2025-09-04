# Trees are essentially LinkedList Nodes with multiple pointers... pointing to left and right
# They can also be thought of as dictionary entries:
# {
#     "value": 4,
#     "left": {
#         "value": 3,
#         "left": None,
#         "right": None
#         },
#     "right": {
#         "value": 23,
#         "left": None,
#         "right": None
#     }
# }
#  If the nodes are only pointing to two other nodes then its a binary tree BUT TREES DONT have to be binary

# FULL tree = Every node points to 2 or 0 nodes, if a node points to 1 node then it is not full
# PERFECT tree = Every node on a level are completely filled
# COMPLETE tree = Tree is filled from left to right with no gaps

# Parent nodes, a child node can be the parent of other children nodes IF there are nodes below it.
# Child nodes, children only have one parent
# Leaf node, these nodes don't have children nodes

# ********************** BIG O ****************************

# Binary Search Tree aka Divide and Conquer = O(log n) best case
#  Worst case is O(n)

# Big O - BST: lookup(), insert(), remove() == 0(log n)

#  ********************** COMPARE LINKED LIST/List to BST (w/o index) ****************************

# Insert() -- You should use LL for this by value
# Lookup() -- BST is better by value
# Remove() -- BST is better again by value