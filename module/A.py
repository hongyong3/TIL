def func():
    print("function A.py")

print(f'A의 __name__은 {__name__}.')
print('top-level A.py')

# A.py에서는 __name__에는 __main__이 A.py가 메인
if __name__ == "__main__":
    print('A.py가 직접 실행.')
else:
    print('B.py가 import 되어 사용됨.')