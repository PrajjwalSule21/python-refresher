"""
Functions
This is the way to isolate code and only be able run the code when needed and called.
"""


# builtin function: these functions are provided by python itself

print("Hello Prajjwal!") # print() is a function which is builtin and used when we need to print something on screen


# Tip: When you hold ctrl button (in windows)/command in (mac) and hover to print function then it will open a file called builtins.py where you can find all the builtin functions.


## Function created by us/users

def my_functions():
    print('Inside my function')


print(my_functions())


def my_function2(first_name, last_name):
    print(f"Hi {first_name} {last_name}, Have a great day!")

print(my_function2(first_name='Prajjwal',
                   last_name='Sule'))

print(my_function2('Prajjwal', "Sule"))


# Scope -> There are scope of variable like where the variable is declared and who it can use it.
# Global: A variable is declared/define out of the function, and it can be used by any method or function.
# Local:  A variable which is declared/define inside any function and can only accessible for that function.


def print_color():
    color = 'RED' #local variable
    print(color)

color = 'BLUE' #global variable

print(color) # this uses global variable so it will give BLUE.
print(print_color()) # this will print RED, cause it uses a local variable.


def print_numbers(highest_num, lowest_num):
    print(highest_num)
    print(lowest_num)

print(print_numbers(highest_num=21, lowest_num=12)) # ideal way to call a function


# function which hold value so that we can refer it to variable

def multiply_numbers(a, b):
    return  a * b

solution = multiply_numbers(a=21, b=12)
print(solution)



def buy_items(cost_of_items):
    return cost_of_items + add_tax_to_items(cost_of_items)

def add_tax_to_items(cost_of_items):
    current_tax_rate = .03
    return cost_of_items * current_tax_rate

final_cost = buy_items(50)
print(final_cost)






