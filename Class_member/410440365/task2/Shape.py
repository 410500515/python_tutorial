from abc import ABC, abstractmethod
import math

# 抽象父類別
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

# Square 類別
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2

    def get_perimeter(self):
        return 4 * self.side_length

# Circle 類別
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * math.pi * self.radius

# EquilateralTriangle 類別
class EquilateralTriangle(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return (math.sqrt(3) / 4) * self.side_length ** 2

    def get_height(self):
        return (math.sqrt(3) / 2) * self.side_length

    def get_perimeter(self):
        return 3 * self.side_length
