"""
Inheritance:
- inheriting attributes and methods form the base class/parent class
- derived/child class can have its own attributes and methods

class <<ChildClassName>>(BaseClass):
    def __init__(self):
        super().__init__(param)

class <<ChildClassName>>(BaseClass):
    def __init__(self):
        BaseClass().__init__(param)
"""
"""
class rectangle:
attributes - length & breadth
methods - perimeter, area

child class = Parallelogram
- inherits from rectangle
- attributes = heights
- volume
"""

class Rectangle:
    def __init__(self, len = 5, brd = 6):
        self.length = len
        self.breadth = brd

    def perimeter(self):
        return 2* (self.length + self.breadth)

    def area(self):
        return self.breadth * self.length

    def show(self):
        print(f"Rectangle Info: \n"
              f"Length: {self.length}\n"
              f"Breadth: {self.breadth}\n"
              f"Area: {self.area()}\n"
              f"Perimeter: {self.perimeter()}")

class Parallelogram(Rectangle):
    def __init__(self, len, brd, height):
        super().__init__(len, brd)
        self.height = height

    def volume(self):
       return self.length * self.breadth * self.height

    @classmethod
    def show(cls):
        cls.show()


rect1 = Rectangle(10, 8)
rect1.show()

