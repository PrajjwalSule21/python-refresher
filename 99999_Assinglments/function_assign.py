"""

- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values
"""


def introduction(firstname, lastname, age):
    user_info = {
        "FirstName": firstname,
        "LastName": lastname,
        "Age": age
    }

    return user_info



data = introduction(
    firstname="prajjwal",
    lastname='sule',
    age=28
)

print(data)