'''
set()

Sets are similar to lists but are unordered and cannot contain duplicates.
Uses {}
'''

my_set = {1,2,3,4,4,5,1,2}
print(my_set)

print(len(my_set))

# print(my_set[0]) # this gives error:TypeError: 'set' object is not subscriptable


#delete
my_set.discard(3)
print(my_set) # it delete 3 from set

my_set.clear()
print((my_set)) # delete the entire set

my_new_set = {1,2,3,4,3,0,1,23,34}
print(my_new_set)

#adding in set
my_new_set.add(21)
print(my_new_set)

#add multiple values
my_new_set.update([121,2121])
print(my_new_set)


"""
tuple()
tuples are also similar to lists but to make a tuple we need to use this () instead of square brackets.
We unable to add or update the tuple.
"""


my_tuple = (1,2,2,3,4,5)
print(my_tuple)

print(my_tuple[1]) #this gave 2

#cant add
# my_tuple[1] = 100  #this give error:TypeError: 'tuple' object does not support item assignment

