"""

Write a Python program that can do the following:

- You have $50

- You buy an item that is $15, that has a 3% tax

- Using the print()  Print how much money you have left, after purchasing the item.
"""


cost = 15
tax = .03  # 3% tax, if 30% then it will .3
budget = 50

item_cost = (cost * tax) + cost
left_money = budget - item_cost

print(left_money)