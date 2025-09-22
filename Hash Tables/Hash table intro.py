# 1)Hash tables are one way, meaning you send the key through the hash and it gives you a number (address), but you cannot undo that or send the address to give you the key.
# 2)Hash tables are deterministic, meaning every time we put the certain key in we expect to get that hash.... deterministic means we know the address

# python includes a built in hash table: dictionaries

# Separate chaining: is the idea of dealing with collisions or (2 dictionary entries at the same hash address)
#  A way to address collisions in hash tables, and not have several key/value pairs at the same address is to use 'Linear probing'.... which is a type of Open Addressing, where if the hash address already has a slot the is occupied, you move to the next spot to check if its occupied, and so forth...until you find one.