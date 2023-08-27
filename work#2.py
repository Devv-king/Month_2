class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        circle_square = 3.14*(self.__radius**2)
        return circle_square

    def info(self):
        return (f"Circle radius: {self.__radius}{self.unit}, "
                f"area: {self.calculate_area()}{self.unit}.")


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        triangle_square = 1/2 * (self.__side_a * self.__side_b)
        return triangle_square

    def info(self):
        return (f"RightTriangle side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit}, "
                f"area: {self.calculate_area()}{self.unit}.")


circle_list = [2, 3]
for i in circle_list:
    circle = Circle(i)
    print(circle.info())

triangle = [[3, 4], [4, 5], [5, 6]]
for a, b in triangle:
    triangle = RightTriangle(a, b)
    print(triangle.info())
