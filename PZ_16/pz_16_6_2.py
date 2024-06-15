# Создание базового класса "Фигура" и его наследование для создания классов "Квадрат",
# "Прямоугольник" и "Круг". Класс "Фигура" будет иметь общие методы, такие как вычисление площади
# и периметра, а классы-наследники будут иметь специфичные методы и свойства.
import math

class Figure:
    def __init__(self):
        pass

    def area(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

print("Выберите фигуру:")
print("1. Квадрат")
print("2. Прямоугольник")
print("3. Круг")

choice = int(input("Введите ваш выбор (1-3): "))

if choice == 1:
    side_length = float(input("Введите длину стороны квадрата: "))
    square = Square(side_length)
    print("Площадь квадрата равна:", square.area())
elif choice == 2:
    width = float(input("Введите ширину прямоугольника: "))
    height = float(input("Введите высоту прямоугольника: "))
    rectangle = Rectangle(width, height)
    print("Площадь прямоугольника равна:", rectangle.area())
elif choice == 3:
    radius = float(input("Введите радиус круга: "))
    circle = Circle(radius)
    print("Площадь круга равна:", circle.area())
else:
    print("Неверный выбор.")
