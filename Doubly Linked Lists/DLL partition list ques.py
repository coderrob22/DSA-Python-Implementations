# DLL: Partition List ( ** Interview Question)
# Write a method called partition_list(self, x) that rearranges the nodes in a doubly linked list so that all nodes with a value less than a given number x come before all nodes with a value greater than or equal to x.

# You must maintain the original relative order of the nodes in each of the two partitions.

# The partitioning must be performed in-place. You cannot create new nodes (other than dummy nodes).

# Both .next and .prev pointers must be updated correctly.

# If the list is empty, nothing should happen.





# 🧪 Examples

# Example 1
# Input DLL:
# 3 <-> 8 <-> 5 <-> 10 <-> 2 <-> 1
# Partition value: x = 5
# Output DLL:
# 3 <-> 2 <-> 1 <-> 8 <-> 5 <-> 10

# Why:

# Nodes < 5: 3, 2, 1

# Nodes >= 5: 8, 5, 10

# Order of nodes is preserved in both groups

# Smaller group comes before larger/equal group



# Example 2
# Input DLL:
# 1 <-> 2 <-> 3
# Partition value: x = 5
# Output DLL:
# 1 <-> 2 <-> 3
# Why:
# All nodes are already less than x. No rearrangement needed.



# Example 3
# Input DLL:
# 7 <-> 8 <-> 9
# Partition value: x = 5
# Output DLL:
# 7 <-> 8 <-> 9
# Why:
# All nodes are >= x. Order remains the same.



# Example 4
# Input DLL:
# 1
# Partition value: x = 2
# Output DLL:
# 1
# Why:
# Single-node list. Nothing to rearrange.



# Example 5
# Input DLL:
# (empty)
# Partition value: x = 3
# Output DLL:
# (empty)
# Why:
# Empty list. Nothing to do.





# 📘 What This Exercise Is Designed to Teach

# How to traverse and reorganize nodes in a doubly linked list.

# How to use dummy nodes to simplify pointer manipulation.

# How to maintain both .next and .prev pointers correctly in DLLs.

# How to perform an in-place partition without losing any nodes.

def partition_list(self, x):
        if not self.head:
            return None
    
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head
    
        while current:
            if current.value < x:
                prev1.next = current
                current.prev = prev1
                prev1 = current
                
            else:
                prev2.next = current
                current.prev = prev2
                prev2 = current
            current = current.next
        
        prev1.next = dummy2.next
        if dummy2.next:
            dummy2.next.prev = prev1
        prev2.next = None
        
        self.head = dummy1.next
        self.head.prev = None