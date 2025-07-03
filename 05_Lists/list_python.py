"""
List are collection of data represents by [], it can store anything inside the [], as well we don't need to define the type of list.
The difference between list and array is, in array before storing any data we need to define the type of data we want to store.
But in list we can store anything without defining.

It always starts with index 0
From backwards it starts with index -1
"""


my_list = [12,23,45,12,34,5,3,1,3,5]
print(type(my_list))

print(my_list)

my_list2 = ['Prajjwal', "Sule"]
print(my_list2)


mix_list = ['Prajjwal', 21, "Sule", 0.3]
print(mix_list)


print(my_list[0]) # give me 12
print(my_list[-1]) #give me 5


# We can change any item after defining a list

people = ['Aric', "John", "Karl"]
print(people) # This gave me ['Aric', "John", "Karl"]

people[0] = "Prajjwal"
print(people) # This gave me ['Prajjwal', 'John', 'Karl']


# finding length of a list
print(len(people))



# Slicing -> its first arugment is included and last is exluded, like [0,2] so it will take 0th index item and 1st index item.
print(people[0:2]) # this gave ['Prajjwal', 'John']


# add, delete, and insert on specific position from list

people.append('Sule')
print(people) #this gave ['Prajjwal', 'John', 'Karl', 'Sule']

people.pop() # It will pop out last item of a list
print(people) #this gave ['Prajjwal', 'John', 'Karl']


people.insert(1, "Sule")
print(people) # this gave ['Prajjwal', 'Sule', 'John', 'Karl']

people.remove('John') #it will remove the item we specify
print(people) #this gave ['Prajjwal', 'Sule', 'Karl']

people.pop(0) #it will pop out 0th index item
print(people) # this gave ['Sule', 'Karl']


# sorting the list

my_list.sort()
print(my_list) # this gave [1, 3, 3, 5, 5, 12, 12, 23, 34, 45]
