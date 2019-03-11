import sys
sys.stdin = open("홀수만 더하기_input.txt", "r")
for test_case in range(int(input())):
    data = list(map(int, input().split()))
    sum = 0
    for i in range(len(data)):
        if data[i] % 2:
            sum += data[i]
    print("#{} {}".format(test_case+1 ,sum))