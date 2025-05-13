from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass
    # def get_perimeter(self):
    #     pass
    # def get_height(self):
    #     pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return 4 * self.side

    def __str__(self):
        return f"Square(side_length={self.side})"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"

class EquilateralTriangle(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return (math.sqrt(3) / 4) * self.side ** 2

    def get_height(self):
        return (math.sqrt(3) / 2) * self.side

    def get_perimeter(self):
        return 3 * self.side

    def __str__(self):
        return f"EquilateralTriangle(side_length={self.side})"
