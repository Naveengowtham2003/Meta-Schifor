import math # Example for encapsulation and abstraction
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass  # Abstract method
    def perimeter(self):
        pass  # Abstract method
    def get_name(self):
        return self.name
class Rectange(Shape): # Example for polymorphism
    def __init__(self, name, width, height):
        super().__init__(name)
        self._width = width
        self._height = height
    def area(self):
        return int(self._width * self._height)
    def perimeter(self):
        return int(2 * (self._width + self._height))
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self._radius = radius
    def area(self):
        return int(math.pi * self._radius ** 2)
    def perimeter(self):
        return int(2 * (math.pi * self._radius))
class Square(Rectange):# Example for Multiple InheritanceD
    def __init__(self, name, side):
        super().__init__(name, side, side)
rectange = Rectange("Rectange", 4, 2)
circle = Circle("circle", 6)
square = Square("Square", 3)
print("------------------------------------------------------------------------------------------------")
print(rectange.get_name(),"\n","Area:",rectange.area(),"\n","Perimeter:",rectange.perimeter())
print("------------------------------------------------------------------------------------------------")
print(circle.get_name(),"\n","Area:",circle.area(),"\n","Perimeter:",circle.perimeter())
print("------------------------------------------------------------------------------------------------")
print(square.get_name(),"\n","Area:",square.area(),"\n","Perimeter:",square.perimeter())
print("------------------------------------------------------------------------------------------------")
