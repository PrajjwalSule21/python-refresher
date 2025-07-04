"""

String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days.
"""


days = input("How many days until your Birthday: ")
# as input() takes string even if number it will think at is string, so we need to type cast before diving with int().

weeks = int(days) // 7   # // -> This give exact number not in floating digit
print(f"Great! You have {weeks} weeks in your Birthday")