import math
from Shape_File import Shape


class Circle(Shape):
    def __init__(self, radius: float):
        if radius > 0:
            self.__radius = radius
            self.__valid = True
        else:
            print('Error : radius cannot be negative!')
            self.__valid = False

    def set_radius(self, radius: float):
        if radius > 0:
            self.__radius = radius
            self.__valid = True
        else:
            print('Error : radius cannot be negative!')
            self.__valid = False

    def get_radius(self) -> float:
        return self.__radius

    def area(self) -> float:
        return pow(self.__radius, 2) * math.pi

    def parameter(self) -> float:
        return 2 * math.pi * self.__radius

    def display(self):
        if self.__valid:
            print(f'Circle information : \nArea = {self.area()} cm \nCircumference = {self.parameter()} cm')
            print('------------------------------------------------')
