class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    @staticmethod
    def is_square(width, height):
        return width == height

    @classmethod
    def create_square(cls, side_length):
        return cls(side_length, side_length)


rectangle1 = Rectangle(4, 6)
rectangle3 = Rectangle(3, 3)
print(f"Площадь прямоугольника: {rectangle1.calculate_area()}")
print(f"Периметр прямоугольника: {rectangle1.calculate_perimeter()}")

rectangle2 = Rectangle.create_square(5)
print(f"Площадь квадрата: {rectangle2.calculate_area()}")

is_square = Rectangle.is_square(rectangle3.width, rectangle3.height)
print(f"Является ли ({rectangle3.width}x{rectangle3.height}) квадратом? {is_square}")
