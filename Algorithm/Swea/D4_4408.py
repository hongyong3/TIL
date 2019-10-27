import sys
sys.stdin = open("D4_4408_input.txt", "r")

T = int(input())
for test_case in range(1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # room = [[0] * 200 for _ in range(200)]
    room1 = [0] * 200
    # print(room1[data[0][0]: data[0][1]])

    for i in range(N):
        room1[data[i][0]: data[i][1]] = 1
    print(room1)