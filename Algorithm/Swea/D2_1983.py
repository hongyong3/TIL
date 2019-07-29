import sys
sys.stdin = open("D2_1983_input.txt", "r")

T = int(input())
for test_case in range(T):
    grades = ["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
    N, K = list(map(int, input().split()))
    avg = [0] * N
    data = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        avg[i] = int((data[i][0] * 35 + data[i][1] * 45 + data[i][2] * 20))
    for j in range(N):
        if avg[K-1] == list(reversed(sorted(avg)))[j]:
            print("#{} {}".format(test_case + 1, grades[int(j / (N / 10))]))