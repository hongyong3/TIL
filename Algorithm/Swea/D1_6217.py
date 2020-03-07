class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return "이름: {}".format(self.__name)

class GraduateStudent(Student):
    def __init__(self, name, major):
        Student.__init__(self, name)
        self.__name = name
        self.__major = major

    @property
    def major(self):
        return self.__major

    def __repr__(self):
        return "이름: {}, 전공: {}".format(self.__name, self.__major)

student = Student("홍길동")
print(student)
student = GraduateStudent("이순신", "컴퓨터")
print(student)