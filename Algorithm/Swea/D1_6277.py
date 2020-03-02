import sys
sys.stdin = open("D1_6277_input.txt", "r")

data = list(int(input()) for _ in range(5))
print("입력된 값 {}의 평균은 {}입니다.".format(data, sum(data) / 5))