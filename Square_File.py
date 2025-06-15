from Shape_File import Shape


class Square(Shape):
    def __init__(self, side: float):
        if side > 0:
            self.__side = side
            self.__valid = True
        else:
            print('Error : side cannot be negative!')
            self.__valid = False

    def set_side(self, side: float):
        if side > 0:
            self.__side = side
        else:
            print('Error : side cannot be negative!')

    def get_side(self) -> float:
        return self.__side

    def area(self) -> float:
        return pow(self.__side, 2)

    def parameter(self) -> float:
        return 4 * self.__side

    def display(self):
        if self.__valid:
            print(f'Square information : \nArea = {self.area()} cm \nParameter = {self.parameter()} cm')
            print('------------------------------------------------')
