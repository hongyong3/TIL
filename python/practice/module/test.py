def add(a, b):
    return a+b

def mul(a, b):
    return a * b


# 프로그램의 시작점일때만 아래 코드가 실행
if __name__ == '__main__':
    print(add(10, 20))
    print(mul(10, 20))

# 이 스크립트 파일을 가져다 사용하면 def에 정의한 함수들을 사용할 수 있다.
# 배쉬 창에 python -i를 입력하고
# import test
# test.add(10, 20)
# 30
# test.mul(10, 20)
# 200