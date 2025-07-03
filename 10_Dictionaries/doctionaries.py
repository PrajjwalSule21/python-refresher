"""
Dictionary have key value pairs
"""

user_dictionary = {
    "username":"Prajjwal21",
    "first_name": "Prajjwal",
    "last_name" : "Sule",
    "age": 28

}

print(user_dictionary)

print(user_dictionary.get("username")) #get value of this key

# add other key

user_dictionary['marries'] = True

print(user_dictionary)

print(len(user_dictionary))

# pop out key and value

user_dictionary.pop('age')
print(user_dictionary) # this will delete age key and its respective value

# clear entire dict

user_dictionary.clear()
print(user_dictionary) #this will give empty dict {}

# delete dict

del user_dictionary
# print(user_dictionary) # this will give error: NameError: name 'user_dictionary' is not defined


new_user_dictionary = {
    "username":"Prajjwal21",
    "first_name": "Prajjwal",
    "last_name" : "Sule",
    "age": 28,
    "married": True

}

for i in new_user_dictionary:
    print(i) # this will only print keys

for i, j in new_user_dictionary.items():
    print(i,j)


for i in new_user_dictionary.keys():
    print(i)

for i in new_user_dictionary.values():
    print(i)


new_user_dictionary2 = new_user_dictionary
new_user_dictionary2.pop("age")

print(new_user_dictionary2)
print(new_user_dictionary)  # the age is deleted from here too, because both variable refer to same memory location, this is how python works


# right way to copy
new_user_dictionary = {
    "username":"Prajjwal21",
    "first_name": "Prajjwal",
    "last_name" : "Sule",
    "age": 28,
    "married": True

}

new_user_dictionary3 = new_user_dictionary.copy() # copy() will allow python interpreter to make separate reference of variables
new_user_dictionary3.pop('age')

print(new_user_dictionary3) # age will gone from here only
print(new_user_dictionary) # age is still there



