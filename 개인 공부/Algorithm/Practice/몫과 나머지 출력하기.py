import sys
sys.stdin = open("몫과 나머지 출력하기_input.txt", "r")
T = int(input())
for test_case in range(T):
    data = list(map(int, input().split()))
    print("#{} {} {}".format(test_case+1, data[0]//data[1], data[0]%data[1]))