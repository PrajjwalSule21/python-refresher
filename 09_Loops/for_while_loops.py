"""
For and While loop

loops are working on iterable objects
"""


my_list = [1,2,3,4,5,6,7,8]

for item in my_list:
    print(item)

for iterator in my_list:
    print(iterator)

for  x in range(3,6): #3 is included and 6 is excluded
    print(x)


sum_my_list = 0
for i in my_list:
    sum_my_list = sum_my_list + i
print(sum_my_list)


#loop through strings


days = ['Monday', 'Tuesday', 'Wednesday']

for x in days:
    print(f'Happy {x}')


new_days = []
for day in days:
    day = day[::-1]
    day = day[3:]
    new_days.append(day[::-1])

print(new_days)



# while loops

i = 0
while i < 5:
    i = i + 1
    print(i)


# continue statement, will make the loop from start

a = 0
while a < 5:
    a = a + 1
    if a == 3:
        continue
    print(a)


# break statement will stop the loop completely


b = 0
while b < 5:
    b = b + 1
    if b == 3:
        continue
    print(b)
    if b == 4:
        break
