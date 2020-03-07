class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return "원의 면적: {}".format(3.14 * pow(self.__radius, 2))

circle = Circle(2)
print(circle.area())