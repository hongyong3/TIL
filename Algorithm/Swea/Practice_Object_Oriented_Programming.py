# # ex1) 딕셔너리 및 리스트 객체를 이용한 코드 생성
#
# # name과 age를 키로 하는 딕셔너리 객체 3개 생성 및
# # members 리스트 객체의 항목으로 구성
# members = [
#     # 딕셔너리 객체는 한 명의 멤버 정보만 다룸
#     {"name": '홍길동', "age": 20}, # => 딕셔너리 객체
#     {"name": '이순신', "age": 45}, # => 딕셔너리 객체
#     {"name": '강감찬', "age": 35}, # => 딕셔너리 객체
# ]
#
# # members 리스트 객체의 각 항목을 member 변수에 저장해 반복 수행
# for member in members:
#     print("{}\t{}".format(member["name"], member["age"]))
#
# # ex2) 딕셔너리 객체의 생성 및 정보 출력
# def create(name, age):  # 멤버 정보 생성이 필요할 때마다 호출하여 사용
#     # create() 함수
#     # 매개변수에 인자를 전달 받아 딕셔너리 객체를 생성 및 반환하는 함수
#     return {"name": name, "age": age}
#
# def to_str(person):
#     # to_str()함수
#     # 인자로 전달 받은 딕셔너리 객체의 값을 문자열로 반환하는 함수
#     return "{}\t{}".format(person["name"], person["age"])
#
# members = [
#     # 딕셔너리 객체는 한 명의 멤버 정보만 다룸
#     create("홍길동", 20),
#     create("이순신", 45),
#     create("강감찬", 35),
# ]
# # members 리스트 객체의 각 항목을 member 변수에 저장
# for member in members:
#     print(to_str(member))   # 각 멤버 정보에 대한 문자열 값 출력

### 클래스 정의 및 객체 생성

# 클래스 정의
# class Person:
#     pass
#
# member = Person() # member 객체 생성; 여기서 Person은 생성자 메서드라고 함
#
# if isinstance(member, Person):  # 첫 번째 인자의 객체가
#                                 # 두 번째 인자의 클래스 인스턴스인지 검사
#     print("member는 Person 클래스의 인스턴스입니다.")
#
### 객체의 생성과 소멸, 그리고 self

# class Person:
#     def __init__(self, name, age):  #  생성자 메서드;
#                                     # self : 객체공간의 참조 전달
#                                     # name, age : 매개변수 인자
#                                     # 즉, self가 가리키는 객체공간에 name, age 필드 생성
#                                     # 객체를 생성하기 위해 호출하는 생성자 메서드 => __init__ 메서드
#         self.name = name
#         self.age = age
#         print("{} 객체가 생성되었습니다.".format(self.name))
#
#    def __del__(self):  # self : 객체공간의 참조 전달
#                        # 객체를 소멸하기 위해 호출하는 소멸자 메서드 => __del__ 메서드
#        print("{} 객체가 제거되었습니다.".format(self.name))
#
# member = Person("홍길동", 20)
#
# print("{}\t{}".format(member.name, member.age))
#
# print(dir(member))

### 클래스와 인스턴스의 특징
## 인스턴스 메서드 정의

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("{} 객체가 생성되었습니다.".format(self.name))
#
#     def __del__(self):
#         print("{} 객체가 제거되었습니다.".format(self.name))
#
#     # 인스턴스 메서드
#     def to_str(self):   # name 필드와 age 필드를 문자열로 반환
#         return "{}\t{}".format(self.name, self.age)
#
# members = [
#     Person("홍길동", 20),
#     Person("이순신", 45),  # Person 클래스의 객체 세 개를 항목으로 가진
#     Person("강감찬", 35),  # members 리스트 객체 생성
# ]
#
# for member in members:      # members 리스트 객체의 각 항목을 member 변수에 저장해 반복 수행
#     print(member.to_str())  # member 객체의 to_str 메서드를 호출해 반환된 문자열 값 출력

## 인스턴스 변수의 접근 제한 기능
# class Person:
#     def __init__(self, name, age):
#         self.__name = name  # 프라이빗 필드 생성
#         self.__age = age    # 프라이빗 필드 생성
#         print("{} 객체가 생성되었습니다.".format(self.__name))
#
#     def __del__(self):
#         print("{} 객체가 제거되었습니다.".format(self.__name))
#
#     def to_str(self):
#         return "{}\t{}".format(self.__name, self.__age)
#
#     def get_name(self):     # __name 필드의 값을 반환하는 getter 메서드
#         return self.__name  # __name 필드에 대해서는 getter 메서드만 제공
#
#     def get_age(self):      # __age 필드의 값을 반환하는 메서드
#         return self.__age
#
#     def set_age(self, age): # __age 필드의 값을 변경하는 메서드
#         if age < 0:
#             raise TypeError("나이는 0이상의 값만 허용합니다.")
#         self.__age = age
#
# members = [
#     Person("홍길동", 20),
#     Person("이순신", 45),
#     Person("강감찬", 35),
# ]
#
# members[0].set_age(-20)
#
# for member in members:
#     print(member.to_str())

## 데코레이터(Decorator) 기능

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         print("{} 객체가 생성되었습니다.".format(self.__name))
#
#     def __del__(self):
#         print("{} 객체가 제거되었습니다.".format(self.__name))
#
#     def to_str(self):
#         return "{}\t{}".format(self.__name, self.__age)
#
#     @property   # 모습은 메서드이지만, 변수처럼 사용 가능
#                 # __name 필드값을 반호나하는 getter 메서드의 역할
#     def name(self):
#         return self.__name
#
#     @property   # __age 필드값을 반호나하는 getter 메서드의 역할
#     def age(self):
#         return self.__age
#
#     @age.setter # 모습은 메서드이지만, 변수처럼 사용 가능
#                 # __age 필드값을 반환하는 setter 메서드의 역할
#     def age(self, age):
#         if age < 0:
#             raise TypeError("나이는 0이상의 값만 허용합니다.")
#         self.__age = age
#
# members = [
#     Person("홍길동", 20),
#     Person("이순신", 45),
#     Person("강감찬", 35),
# ]
#
# members[0].age == 22    # age @ property 데코레이터를 이용해 변수처럼 값 저장
#
# for member in members:
#     print(member.to_str())

## 클래스 변수의 count 활용법

# class Person:
#     count = 0
#
#     def __init__(self, name, age):  # 객체가 생성될 때마다 호출되는 __init__ 메서드
#         self.__name = name
#         self.__age = age
#         Person.count += 1
#         print("{} 객체가 생성되었습니다.".format(self.__name))
#
#     def __del__(self):
#         print("{} 객체가 제거되었습니다.".format(self.__name))
#
#     def to_str(self):
#         return "{}\t{}".format(self.__name, self.__age)
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def age(self):
#         return self.age
#
#     @age.setter
#     def age(self, age):
#         if age < 0:
#             raise TypeError("나이는 0이상의 값만 허용합니다.")
#         self.age
#
# members = [
#     Person("홍길동", 20),
#     Person("이순신", 45),
#     Person("강감찬", 35),
# ]
# print("현재의 Person 클래스의 인스턴스는 총 {} 개입니다.".format(Person.count))

## 클래스 메서드의 사용

# class Person:
#     count = 0
#
#     def __init__(self, name, age):  # 객체가 생성될 때마다 호출되는 __init__ 메서드
#         self.__name = name
#         self.__age = age
#         Person.count += 1
#         print("{} 객체가 생성되었습니다.".format(self.__name))
#
#     def __del__(self):
#         print("{} 객체가 제거되었습니다.".format(self.__name))
#
#     def to_str(self):
#         return "{}\t{}".format(self.__name, self.__age)
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def age(self):
#         return self.age
#
#     @age.setter
#     def age(self, age):
#         if age < 0:
#             raise TypeError("나이는 0이상의 값만 허용합니다.")
#         self.age
#
#     @classmethod
#     def get_info(cls):  # 클래스 참조 정보가 인자로 넘어올 매개변수
#         return "현재 Person 클래스의 인스턴스는 총 {} 개입니다.".format(cls.count)  # cls.count는 Person.count 와 동일
#
# members = [
#     Person("홍길동", 20),
#     Person("이순신", 45),
#     Person("강감찬", 35),
# ]
# print(Person.get_info())    # Person 클래스를 통해 호출

## 비교연산자 오버로딩

# class Person:
#     count = 0
#
#     def __init__(self, name, age):  # 객체가 생성될 때마다 호출되는 __init__ 메서드
#         self.__name = name
#         self.__age = age
#         Person.count += 1
#         print("{} 객체가 생성되었습니다.".format(self.__name))
#
#     def __del__(self):
#         print("{} 객체가 제거되었습니다.".format(self.__name))
#
#     def to_str(self):
#         return "{}\t{}".format(self.__name, self.__age)
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def age(self):
#         return self.age
#
#     @age.setter
#     def age(self, age):
#         if age < 0:
#             raise TypeError("나이는 0이상의 값만 허용합니다.")
#         self.age
#
#     @classmethod
#     def get_info(cls):  # 클래스 참조 정보가 인자로 넘어올 매개변수
#         return "현재 Person 클래스의 인스턴스는 총 {} 개입니다.".format(cls.count)  # cls.count는 Person.count 와 동일
#
#     def __gt__(self, other):
#         return self.__age > other.__age     # self의 __age 필드가 other 객체의 __age 필드보다 크면 True 반환
#
#     def __ge__(self, other):
#         return self.__age >= other.__age    # self의 __age 필드가 other 객체의 __age 필드보다 크거나 같으면 True 반환
#
#     def __lt__(self, other):
#         return self.__age < other.__age     # self의 __age 필드가 other 객체의 __age 필드보다 작으면 True 반환
#
#     def __le__(self, other):
#         return self.__age <= other.__age    # self의 __age 필드가 other 객체의 __age 필드보다 작거나 같으면 True 반환
#
#     def __eq__(self, other):
#         return self.__age == other.__age    # self의 __age 필드가 other 객체의 __age와 같으면 True 반환
#
#     def __ne__(self, other):
#         return self.__age != other.__age  # self의 __age 필드가 other 객체의 __age와 다르면 True 반환
#
# members = [
#     Person("홍길동", 20),
#     Person("이순신", 45),
#     Person("강감찬", 35),
# ]
#
# cnt = len(members)
#
# i = 0
# while True:
#     print("members[{}] > members[{}] => {}".format(i, i + 1, members[i] > members[i + 1]))  # members[i] > members[i + 1] => def __gt__
#     i += 1
#     if i == cnt - 1:
#         print("members[{}] > members[{}] => {}".format(i, 0, members[i] > members[0]))
#
# print(Person.get_info())    # Person 클래스를 통해 호출

## __str()__ 메서드

# class Person:
#     count = 0
#
#     def __init__(self, name, age):  # 객체가 생성될 때마다 호출되는 __init__ 메서드
#         self.__name = name
#         self.__age = age
#         Person.count += 1
#         print("{} 객체가 생성되었습니다.".format(self.__name))
#
#     def __del__(self):
#         print("{} 객체가 제거되었습니다.".format(self.__name))
#
#     def to_str(self):
#         return "{}\t{}".format(self.__name, self.__age)
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def age(self):
#         return self.age
#
#     @age.setter
#     def age(self, age):
#         if age < 0:
#             raise TypeError("나이는 0이상의 값만 허용합니다.")
#         self.age
#
#     @classmethod
#     def get_info(cls):  # 클래스 참조 정보가 인자로 넘어올 매개변수
#         return "현재 Person 클래스의 인스턴스는 총 {} 개입니다.".format(cls.count)  # cls.count는 Person.count 와 동일
#
#     def __gt__(self, other):
#         return self.__age > other.__age     # self의 __age 필드가 other 객체의 __age 필드보다 크면 True 반환
#
#     def __ge__(self, other):
#         return self.__age >= other.__age    # self의 __age 필드가 other 객체의 __age 필드보다 크거나 같으면 True 반환
#
#     def __lt__(self, other):
#         return self.__age < other.__age     # self의 __age 필드가 other 객체의 __age 필드보다 작으면 True 반환
#
#     def __le__(self, other):
#         return self.__age <= other.__age    # self의 __age 필드가 other 객체의 __age 필드보다 작거나 같으면 True 반환
#
#     def __eq__(self, other):
#         return self.__age == other.__age    # self의 __age 필드가 other 객체의 __age와 같으면 True 반환
#
#     def __ne__(self, other):
#         return self.__age != other.__age  # self의 __age 필드가 other 객체의 __age와 다르면 True 반환
#
#     def __str__(self):
#         return "{}\t{}".format(self.__name, self.__age) # 문자열 반환
#
# members = [
#     Person("홍길동", 20),
#     Person("이순신", 45),
#     Person("강감찬", 35),
# ]
#
# for member in members:
#     print(str(member))  # Person 클래스의 객체를 전달하면 __str__메서드 호출

## 클래스 상속
#
# class Parent:
#     def __init__(self, family_name):
#         self.__family_name = family_name
#         print("Parent 클래스의 __init__() ...")
#
#     @property
#     def family_name(self):
#         return self.__family_name
#
# class Child(Parent):
#     def __init__(self, first_name, last_name):
#         Parent.__init__(self, last_name)    # 부모 클래스의 __family_name 필드를 매개변수 last_name 으로 초기화
#         # super().__init__(last_name)       # super() 호출과 생성자 호출을 결합해 동일한 효과 얻음
#         self.__first_name = first_name
#         print("Child 클래스의 __init__() ...")
#
#     @property
#     def first_name(self):
#         return self.__first_name
#
#     @first_name.setter
#     def first_name(self, first_name):
#         self.__first_name = first_name
#
#     @property
#     def name(self): # Parent 클래스의 family_name 속성의 반환 값과
#                     # Child 클래스의 first_name 속성의 반환 값을 문자열로 만들어 반환
#         return "{} {}".format(self.family_name, self.first_name)
#
# child = Child("길동", "홍")
#
# print(child.family_name)
# print(child.first_name)
# print(child.name)
# print("======>")
# child.first_name = "길순"
# print(child.name)

## 메서드 오버라이딩
#
# class Parent:
#     def __init__(self, family_name):
#         self.__family_name = family_name
#         print("Parent 클래스의 __init__() ...")
#
#     @property
#     def family_name(self):
#         return self.__family_name
#
#     def print_info(self):
#         print("Parent: {}".format(self.family_name))
#
# class Child(Parent):
#     def __init__(self, first_name, last_name):
#         Parent.__init__(self, last_name)
#         # super().__init__(last_name)
#         self.__first_name = first_name
#         print("Child 클래스의 __init__() ...")
#
#     @property
#     def first_name(self):
#         return self.__first_name
#
#     @first_name.setter
#     def first_name(self, first_name):
#         self.__first_name = first_name
#
#     @property
#     def name(self):
#         return "{} {}".format(self.family_name, self.first_name)
#
#     def print_info(self):   # 오버라이딩
#         Parent.print_info(self)
#         # super().print_info()
#         print("Child: {}".format(self.name))
#
# child = Child("길동", "홍")
# child.print_info()

### Python Object_Oriented_Programming 실습

# -*- coding: utf-8 -*-

# Practice_Object_Oriented_Programming.py

# Student 클래스
# - Private Field를 가지고 있음
# - 읽기 전용 name, gender Property
# - 일기, 쓰기 모두 가능한 height Property
# - 특수함수 __repr__에 대한 정의를 가짐
#   -> repr 함수는 객체 출력시 주로 사용

class Student:
    def __init__(self, name, gender, height):   # __init__ 생성자 메서드 정의
        self.__name = name  # private Field
        self.__gender = gender
        self.__height = height

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def __repr__(self): # repr 함수는 객체 출력 시 주로 사용
                        # __repr__(self) 함수를 __str__(self)로 바꿔도 동작에는 이상 없음.
        return "{}(name: {}, gender: {}, height: {}"\
            .format(self.__class__.__name__, self.name, self.gender, self.height )

# s1 = Student("홍길동", "남", 176.5)
# print(s1)

## students 리스트 객체 생성

students = [
    Student("홍길동", "남", 176.5),
    Student("강감찬", "남", 182.2),
    Student("이순신", "남", 188.5),
    Student("유관순", "여", 158.4),
]

for student in students:
    print(student)

print()
print("name으로 오름차순 정렬 후 ===>")

# name 기준 오름차순 정렬;
# sorted 함수는 반복가능한 객체 대상
# 사용자 정의 객체 사용 시 해당 리스트 객체에 있는 각 항목에서 키를 사용한 정보 전달
# 함수는 반복되는 객체의 항목을 인자로 받아 수행
for student in sorted(students, key=lambda x: x.name):
    print(student)

print()
print("name으로 내림차순 정렬 후 ===>")

for student in sorted(students, key=lambda x: x.name, reverse = True):
    print(student)

print()
print("height로 오름차순 정렬 후 ===>")

for student in sorted(students, key=lambda x: x.height):
    print(student)

print()
print("height로 내림차순 정렬 후 ===>")

for student in sorted(students, key=lambda x: x.height, reverse = True):
    print(student)
