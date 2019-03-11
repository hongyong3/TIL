import sys
sys.stdin = open("평균값 구하기_input.txt", "r")

for test_case in range(int(input())):
    data = list(map(int, input().split()))
    sum, avg = 0, 0
    for i in range(len(data)):
        sum += data[i]
        avg = sum / len(data)
    print("#{} {:.0f}".format(test_case+1, avg))