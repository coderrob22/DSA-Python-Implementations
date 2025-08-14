# DLL: Reverse Between ( ** Interview Question)
# Write a method reverse_between that reverses a portion of a doubly linked list in place.

# You are given a start index and an end index (inclusive range). Reverse only the nodes between those indices.

# Indexing is zero-based.

# The list is made of nodes with both next and prev pointers.

# Make sure the list remains fully connected after the reversal in both directions.

# If the list has fewer than two nodes or the start and end indices are the same, leave the list unchanged.


# Examples

# Input:  1 <-> 2 <-> 3 <-> 4 <-> 5,  start_index = 1, end_index = 3  
# Output: 1 <-> 4 <-> 3 <-> 2 <-> 5
 
# Input:  10 <-> 20 <-> 30 <-> 40,  start_index = 0, end_index = 2  
# Output: 30 <-> 20 <-> 10 <-> 40
 
# Input:  1,  start_index = 0, end_index = 0  
# Output: 1




# 📘 What This Exercise Is Designed to Teach

# How to manipulate pointers in a doubly linked list

# Understanding in-place reversal using node repositioning

# Careful edge case handling in linked list algorithms

def reverse_between(self, start_index, end_index):
        if self.length <= 1 or start_index == end_index:
            return
 
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
 
        prev = dummy
        for _ in range(start_index):
            prev = prev.next
 
        current = prev.next
 
        for _ in range(end_index - start_index):
            node_to_move = current.next
 
            current.next = node_to_move.next
            if node_to_move.next:
                node_to_move.next.prev = current
 
            node_to_move.next = prev.next
            prev.next.prev = node_to_move
            prev.next = node_to_move
            node_to_move.prev = prev
 
        self.head = dummy.next
        self.head.prev = None