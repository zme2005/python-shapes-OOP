from Circle_File import Circle
from Shape_File import Shape
from Square_File import Square
from Rectangle_File import Rectangle

shapes = [Circle(2.5), Square(4), Rectangle(3.4, 7.2)]
for shape in shapes:
    if isinstance(shape, Shape):
        shape.display()
