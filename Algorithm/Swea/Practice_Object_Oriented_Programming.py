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

class Person:
    def __init__(self, name, age):  #  생성자 메서드;
                                    # self : 객체공간의 참조 전달
                                    # name, age : 매개변수 인자
                                    # 즉, self가 가리키는 객체공간에 name, age 필드 생성
        self.name = name
        self.age = age
        print("{} 객체가 생성되었습니다.".format(self.name))

    def __del__(self):  # self : 객체공간의 참조 전달
        print("{} 객체가 제거되었습니다.".format(self.name))

member = Person("홍길동", 20)

print("{}\t{}".format(member.name, member.age))

print(dir(member))