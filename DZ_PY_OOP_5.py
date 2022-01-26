from abc import ABC, abstractmethod
import math


class Shape(ABC):


    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def painting(self):
        pass

    @abstractmethod
    def print_info(self):
        pass


class Square(Shape):
    def __init__(self, name, x=0, color='red'):
        self.name = name
        self.x = x
        self.color = color

    def perimeter(self):
        return self.x * 4

    def square(self):
        return self.x ** 2

    def painting(self):
        for p in range(self.x, 0, -1):
            print(self.x * '*')

    def print_info(self):
        print(f"==={self.name}===\nСторона: {self.x}\nЦвет: {self.color}\nПлощадь: {self.square()}\nПериметр: {self.perimeter()}")
        self.painting()
        print()


class Rectangle(Shape):
    def __init__(self, name, x=0, y=0, color='red'):
        self.name = name
        self.x = x
        self.y = y
        self.color = color

    def perimeter(self):
        return 2 * (self.x + self.y)

    def square(self):
        return self.x * self.y

    def painting(self):
        for p in range(self.x, 0, -1):
            print(self.y * '*')

    def print_info(self):
        print(f"==={self.name}===\nСторона: {self.x}\nШирина: {self.y}\nЦвет: {self.color}\n"
              f"Площадь: {self.square()}\nПериметр: {self.perimeter()}")
        self.painting()
        print()


class Triangle(Shape):
    def __init__(self, name, x=0, y=0, z=0, color='red'):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.color = color

    def perimeter(self):
        return self.z + self.y + self.x

    def square(self):
        d = self.perimeter() / 2
        return round(math.sqrt(d * (d - self.x) * (d - self.y) * (d - self.z)), 2)

    def painting(self):
        for p in range(0, self.y+1):
            print(' ' * (self.y - p), '* ' * p)

    def print_info(self):
        print(f"==={self.name}===\nСторона 1: {self.x}\nСторона 2: {self.y}\nСторона 3: {self.z}\nЦвет: {self.color}\n"
              f"Площадь: {self.square()}\nПериметр: {self.perimeter()}")
        self.painting()


v1 = Square("Квадрат", 3, "red")
v2 = Rectangle("Прямоугольник", 3, 7, "green")
v3 = Triangle("Треугольник", 11, 6, 6, "yellow")

for i in (v1, v2, v3):
    i.print_info()

