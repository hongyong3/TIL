class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return "사각형의 면적: {}".format(self.__width * self.__height)

rectangle = Rectangle(4, 5)
print(rectangle.area())