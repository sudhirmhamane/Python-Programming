'''
Sets in python

Set in python is the collection of non-repetitive elements.

it dont takes the values double time 
ex-> set = {2,3,4,5,5,5,5} 
if we print this set then,
the output will come => {1,2,3,4,5} 

sets don't follows the order.

Properties of sets:
    Sets are unordered - elements order doesn't matter
    Sets are unindexed - cannot access elements by index
    there is no way to change items in set s.
    Sets cannot contain duplicate values.

'''

s = {} # empty dictionary

# marks = {1,3,4,5}

emptySet = set() # empty set

s = {1,2,4,5,6,7,7,7,8,88,8,89,9}
print(s)

# len gives the length of set
print(len(s))

# it remove the given value and update the set.
s.remove(1)
print(s)

# clear method is used to empty the set.
s.clear()
print(s)