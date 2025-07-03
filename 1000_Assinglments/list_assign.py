'''
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals
'''

zoo = ['Tiger', 'Lion', "Bear", 'Leopard', "Crocodile"]

zoo.pop(3) # this delete Leopard

print(zoo)

zoo.append('Dear')

print(zoo)

zoo.remove('Tiger')
print(zoo)

print(zoo)


print(zoo[0:3]) #this will start from 0th and end at 2nd