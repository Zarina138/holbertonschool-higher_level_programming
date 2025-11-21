#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        Radius = abs(self.radius)
        return math.pi * (Radius ** 2)

    def perimeter(self):
        Radius = abs(self.radius)
        return 2 * math.pi * Radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + self.height

def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
