"""
Object oriented programming
Object has properties and methods.
    An object is an instance of a class

Class is a blueprint for creating objects

Advantages of OOP:
- help you bundle functionalities together
- easy creation of a class instance object
- ability to modify methods of a class without changing the class
- create user-defined data structure

car: class
- minimum size - maximum size
- 4 tires/wheels
- windows and a windshield
- headlights
- maximum and minimum seating
- steering wheel

objects: Hyundai, Subaru, Toyota, Mercedes, Tesla, Volvo, Women

Students: class
- Cohort
- Course
- Location
- method - remote/physical

objects: DS Estonia 1, DS Estonia 2, DS PH, Python

class <<Class_name>>: class name should start with Capital Letter
    pass

class has methods - functions defined in the body of the class.
    First argument in the function if self
has attributes - variables defined in a class

__init__ - constructor

- num of doors
- maximum speed
- maximum passengers
- name

def <<method_name>>(self

Instance variables are for data unique to each instance
class variables are for attributes and methods shared by all instances of a class
"""

class Car:
    accelerate = 15 # class variable
    def __init__(self, name, num_doors=4, exotic= False):
        self.name = name
        self.door_no = num_doors
        self.is_exotic = exotic
        self.in_motion = False
        self.speed = 0

    def doors(self):
        if self.door_no not in [2,3,4]:
            return f"{self.name} has invalid door numbers"
        return self.door_no

    def drive(self):
        self.in_motion = True

    def acceleration(self):
        if self.in_motion:
            self.speed += self.accelerate

    def stop(self):
        self.in_motion = False

car1 = Car(name="Toyota Prius", num_doors=4)
car2 = Car(name="Tesla Roadster", num_doors=2, exotic=True)
print(car1)
car2.drive()
car2.acceleration()

car1.drive()
car1.acceleration()
print(car1.speed)
print(car2.speed)