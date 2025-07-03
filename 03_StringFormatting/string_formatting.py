"""

String Formatting is technique to keep a string in a single message without breaking the flow of message.
"""
from traceback import print_tb

first_name = "Prajjwal"
print("Hello " + first_name)


#fstring
print(f'Hello {first_name}')


#format
sentence = "Hello {}"
print(sentence.format(first_name))


"""
In the format you have to maintain the sequence
"""
sentence2 = 'Hi {} {}, nice to meet you!'
last_name = "Sule"
print(sentence2.format(first_name, last_name))

#without maintaining sequence
print(sentence2.format(last_name, first_name))
# this will print Hi Sule Prajjwal, nice to meet you!
