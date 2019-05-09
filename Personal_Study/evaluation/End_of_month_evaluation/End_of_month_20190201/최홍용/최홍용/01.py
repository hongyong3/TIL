# 파일명 변경 금지
# 아래에 클래스를 Point와 Circle을 선언하세요.
# Point의 출력은 Point: (x, y)
# Circle의 출력은 Circle: (x, y), r: r
# 으로 맞춰주세요.
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = int(x)
        self.y = int(y)
    
    def __str__(self):
        return f'Point: {(self.x, self.y)}'

class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r
    
    def get_area(self):
        return 3.14*(self.r)**2

    def get_perimeter(self):
        return 3.14*2*(self.r)

    def get_center(self):
        return (self.center.x, self.center.y)

    def __str__(self):
        return f'Circle: {(self.center.x, self.center.y)}, r: {self.r}'
            







# 아래의 코드는 출력 결과를 확인하기 위한 코드입니다.
# 수정하지마세요. 
if __name__ == '__main__':
    p1 = Point(0, 0)
    c1 = Circle(p1, 3)
    print(c1.get_area())
    print(c1.get_perimeter())
    print(c1.get_center())
    print(c1)
    p2 = Point(4, 5)
    c2 = Circle(p2, 1)
    print(c2.get_area())
    print(c2.get_perimeter())
    print(c2.get_center())
    print(c2)