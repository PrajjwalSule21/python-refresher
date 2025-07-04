"""
Composition
A class contains objects of other classes as its members. This creates a "has-a" relationship, meaning one object "has" another object as part of its structure. It allows for building complex objects from simpler, reusable components, promoting code reusability and flexibility without relying on inheritance.
A way to create objects made up of other objects.
Tn composition, a class contains one or more objects of another class as instance variable
Provide layered functionality to the object
Known as a HAS-A relationship


Explanation:
Imagine building a car.
Instead of saying a Car is a type of Engine (inheritance),
you say a Car has an Engine and has Wheels.
The Car class then uses the functionality provided by its Engine and Wheel objects.

"""

class Engine:
    def start(self):
        print("Engine starting...")

    def off(self):
        print("Engine is off...")

class Wheel:
    def rotate(self):
        print("Wheel rotating...")

    def stop(self):
        print("Wheels are stoped!")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car "has-a" Engine
        self.front_left_wheel = Wheel() # Car "has-a" Wheel
        self.front_right_wheel = Wheel()
        self.rear_left_wheel = Wheel()
        self.rear_right_wheel = Wheel()
        self.all_wheels = Wheel()

    def drive(self):
        self.engine.start()
        self.front_left_wheel.rotate()
        self.front_right_wheel.rotate()
        self.rear_left_wheel.rotate()
        self.rear_right_wheel.rotate()
        print("Car is driving!")
        self.all_wheels.stop()
        self.engine.off()

# Create a Car object
my_car = Car()
my_car.drive()
