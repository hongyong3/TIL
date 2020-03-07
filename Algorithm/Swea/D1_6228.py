class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.__length = length

    def area(self):
        Shape.area(self)
        return "정사각형의 면적: {}".format(pow(self.__length, 2))

square = Square(3)
print(square.area())