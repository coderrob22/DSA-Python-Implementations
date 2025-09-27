# You are given 2 lists: [1,3,5] and [2,4,5]. We want to know do these 2 lists have a number in common...?
# Approach 1 is the easier, less efficient method.... 2 loops, O(n^2)

# Inefficient method: Big O: O(n^2)
def item_in_common(list1, list2):
    for i in range(list1):
        for j in range(list2):
            if i == j:
                return True
    return False

# This is the method interviewers will want to see.... Big O: O(n)...more efficient
def item_in_common2(list1, list2):
    my_dict = {}

    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True
    return False
