#Pseduo Code for using the pop method

# Since there isn't a way to move the tail backwards you must start from head and iterate over all the dictionary next values until you get to 'Next' before your desired value.

# Essentially, there must be another value (pre and temp) that keeps track of the values that are being looped over. Pre will keep track of the value before the last one. Temp will keep track of the last value. Once temp is popped off and Next is None, temp must keep track of the value that is no longer in the list...while Pre must keep track of the value that IS NOW the last value and call that. 

# Something like this visual:

#                  temp
#  11 -> 3 -> 23 -> 7 -> None
#            pre