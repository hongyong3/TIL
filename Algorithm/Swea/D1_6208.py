class Korean:
    def __init__(self, name, nationality):
        self.__name = name
        self.__nationality = nationality

    def __del__(self):
        pass

    # def to_str(self):
    #     return "{}".format(self.__nationality)

    def __repr__(self):
        return "{}".format(self.__nationality)

people = [
    Korean("사람1", "대한민국"),
    Korean("사람2", "대한민국"),
]

for person in people:
    print(person)