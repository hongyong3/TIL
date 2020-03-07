class Person:
    def getGender(self):
        return "Unknown"

class Male(Person):
    def __init__(self, gender):
        self.__gender = gender

    def getGender(self):
        Person.getGender(self)
        return "{}".format(self.__gender)

class Female(Person):
    def __init__(self, gender):
        self.__gender = gender

    def getGender(self):
        Person.getGender(self)
        return "{}".format(self.__gender)

gender = Male("Male")
print(gender.getGender())
gender = Female("Female")
print(gender.getGender())