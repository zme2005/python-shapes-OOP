from Shape_File import Shape


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        if length > 0 and width > 0:
            self.__length = length
            self.__width = width
            self.__len_valid = True
            self.__wid_valid = True
        else:
            print('Error : neither length or width can be negative!')
            self.__len_valid = False
            self.__wid_valid = False

    def set_length(self, length: float):
        if length > 0:
            self.__length = length
        else:
            print('Error : neither length or width can be negative!')
            self.__length = 0

    def get_length(self) -> float:
        return self.__length

    def set_width(self, width: float):
        if width > 0:
            self.__width = width
        else:
            print('Error : neither length or width can be negative!')
            self.__width = 0

    def get_width(self) -> float:
        return self.__width

    def area(self) -> float:
        return self.__length * self.__width

    def parameter(self) -> float:
        return (self.__length + self.__width) * 2

    def display(self):
        if self.__len_valid == True or self.__wid_valid == True:
            print(f'Rectangle information : \nArea = {self.area()} cm \nParameter = {self.parameter()} cm')
            print('------------------------------------------------')
