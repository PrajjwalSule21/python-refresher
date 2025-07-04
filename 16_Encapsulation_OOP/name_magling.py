"""
Name Mangling example
"""

class MyClass:
    def __init__(self):
        self.__private_data = "This is private data"
        self.public_data = "This is public data"

    def get_private_data(self):
        return self.__private_data

# Create an instance of MyClass
obj = MyClass()

# Accessing public data directly works
print(obj.public_data)

# Trying to access mangled private data directly will result in an AttributeError
try:
    print(obj.__private_data)
except AttributeError as e:
    print(f"Error: {e}")

# Accessing private data through a method works as expected
print(obj.get_private_data())

# You can still access the mangled name if you know it
print(obj._MyClass__private_data)


"""
Terminal Output:

This is public data
Error: 'MyClass' object has no attribute '__private_data'
This is private data
This is private data

"""
